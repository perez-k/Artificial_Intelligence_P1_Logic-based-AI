import sys, random

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var in self.domains:
            for val in list(self.domains[var]):
                if len(val) != var.length:
                    self.domains[var].remove(val) 


    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = False
        if self.crossword.overlaps[x, y] != None:
            for xval in list(self.domains[x]):
                o = self.crossword.overlaps[x, y]
                if all(xval[o[0]] != yval[o[1]] for yval in self.domains[y]):
                    self.domains[x].remove(xval) 
                    revised = True   
    
        return revised  
       

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        queue = list()
        if arcs is None:
            for var in self.crossword.variables:
                for nbvar in self.crossword.neighbors(var):
                    queue.append((var, nbvar))
        else:
            queue = arcs.copy()      

        while len(queue) != 0:
            (x, y) = queue[0]
            del queue[0]

            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
            
                b = self.crossword.neighbors(x)
                b.discard(y)
                if len(b) != 0:
                    for z in list(b):
                        queue.append((z, x))

        return True            


    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        if len(assignment) == len(self.domains):
            return True
        return False

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        V = list()
        for var in assignment:
            V.append(assignment.get(var) )
        
        if all(V.count(val) == 1 for val in assignment.values()): # If all values are distinct
            if all(len(assignment[var]) == var.length for var in assignment):  # If every value is the correct length
                if len(assignment) >= 2: 
                    arcs = list() 
                    for var in assignment:
                        for nbvar in self.crossword.neighbors(var):
                            if nbvar in assignment.keys():
                                arcs.append((var, nbvar))                       
                    
                    while len(arcs) != 0:
                        (x, y) = arcs[0]
                        del arcs[0]
                    
                        o = self.crossword.overlaps[x, y]
                        if assignment[x][o[0]] != assignment[y][o[1]]:
                            return False
                        
                    return True   

                else:
                    return True        

        return False       



    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        dct = dict()
        for val in self.domains[var]:
            x = 0  #  Number of values "val" rule out for neighboring variables.
            for nbvar in self.crossword.neighbors(var):
                if nbvar not in assignment:
                    o = self.crossword.overlaps[var, nbvar]
                    for nbval in self.domains[nbvar]:
                        if val[o[0]] != nbval[o[1]]:
                            x += 1

            dct[val] = x
        dv = list(self.domains[var])
        dv.sort(key=lambda v: dct[v])

        return dv

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        vrlst = list()
        for var in self.domains:
            if var not in assignment:
                vrlst.append(var) 

        vrlst.sort(key=lambda vr: len(self.domains[vr]))
        nvrlst = list()
        for v in vrlst:
            if len(self.domains[v]) == len(self.domains[vrlst[0]]):
                nvrlst.append(v)
        vrlst = nvrlst.copy()   

        if len(vrlst) > 1: # If there is a tie (Choose the variable with the minimum number of remaining values in its domain.)
            vrlst.sort(reverse=True, key=lambda v: len(self.crossword.neighbors(v))) # sort tie variable by their degree 
            nvrlst = list()
            for v in vrlst:
                if len(self.domains[v]) == len(self.domains[vrlst[0]]):
                    nvrlst.append(v)
            vrlst = nvrlst.copy() 

            if len(vrlst) > 1:  # If there is a tie (choose the variable with the highest degree)
                return random.choice(vrlst)  # any of the tied variables are acceptable return values.

            else:
                return vrlst[0]

        else:
            return vrlst[0]     


    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """

        if  self.assignment_complete(assignment):
            return assignment

        var = self.select_unassigned_variable(assignment) 
        for val in self.order_domain_values(var, assignment):
            dct = assignment.copy()
            dct[var] = val
            ifvars = list()
            if self.consistent(dct):
                assignment[var] = val

                arcs = list()
                for avar in assignment:
                    for nvr in self.crossword.neighbors(avar):
                        arcs.append((nvr, avar))
                self.ac3(arcs)
                
                vlst = list()
                for v in self.domains:
                    if v not in assignment:
                        if len(self.domains[v]) == 1:
                            vlst.append(v)
                if len(vlst) != 0:  # If inferences != failure
                    for v in vlst:     # add inferences to assignment
                        ifvars.append(v)    # keep track of the inference make based assignment[var] = val
                        assignment[v] = list(self.domains[v])[0]  

                result = self.backtrack(assignment)
                if result != None:
                    return result

            for ifvar in ifvars:        # remove inferences from assignment
                assignment.pop(ifvar)        
            
        return None           

       


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
