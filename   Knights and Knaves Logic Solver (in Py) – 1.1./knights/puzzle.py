from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And( 
    # A can be a knight or a knave, not both  
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),

    # A is a Knight if only if A is a Knight and a Knave    
    Biconditional(AKnight, And(AKnight, AKnave)),
    # A is a Knave if only if A is not a Knight and a Knave   
    Biconditional(AKnave, Not(And(AKnight, AKnave)))
)
# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And( 
    # A can be a knight or a knave, not both  
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
    # B can be a knight or a knave, not both  
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
    
    # A is a Knight if and only if A and B are both knaves
    Biconditional(AKnight, And(AKnave, BKnave)),
    # A is a Knight if and only if A and B are not both knaves
    Biconditional(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(  
       # A can be a knight or a knave, not both  
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
       # B can be a knight or a knave, not both  
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
    
    # A is a Knight if and only if A and B are both Knights or both Knaves
    Biconditional(AKnight, And(Or(And(AKnight, BKnight), And(AKnave, BKnave)), 
        Not(And(And(AKnight, BKnight), And(AKnave, BKnave))))),
 
    # A is a Knave if and only if A and B are not both Knights or both Knaves   
    Biconditional(AKnave, Not(And(Or(And(AKnight, BKnight), And(AKnave, BKnave)),
        Not(And(And(AKnight, BKnight), And(AKnave, BKnave)))))),
   
    # B is a Knight if and only if A and B are not both Knights or both Knaves
    Biconditional(BKnight, And(Or(And(AKnight, BKnave), And(AKnave, BKnight)), 
        Not(And(And(AKnight, BKnave), And(AKnave, BKnight))))),

    # B is a Knave if and only if A and B are both Knights or both Knaves
    Biconditional(BKnave, Not(And(Or(And(AKnight, BKnave), And(AKnave, BKnight)), 
        Not(And(And(AKnight, BKnave), And(AKnave, BKnight))))))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A can be a knight or a knave, not both  
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
    # B can be a knight or a knave, not both  
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
    # C can be a knight or a knave, not both  
    Or(CKnight, CKnave), Not(And(CKnight, CKnave)),

    # A is a Knight if and only if  A is a Knight or Knave
    Biconditional(AKnight, And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)))),
    # A is a Knave if and only if  A is not a Knight or Knave
    Biconditional(AKnave, Not(And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))))),
    
    # B is a Knight if and only if  C is a Knave
    Biconditional(BKnight, CKnave),
    # B is a Knave if and only if C is not a Knave 
    Biconditional(BKnave, Not(CKnave)),


    # C is a Knight if and only if  A is a Knight  
    Biconditional(CKnight, AKnight),
    # C is a Knave if and only if  A is not a Knight  
    Biconditional(CKnave, Not(AKnight))
)



def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}") 


if __name__ == "__main__": 
    main()   