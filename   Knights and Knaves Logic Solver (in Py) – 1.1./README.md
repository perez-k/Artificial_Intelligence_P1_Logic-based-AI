## **Knights and Knaves Logic Solver** – CS50 AI (Propositional Logic)

---

### **Description**  
A Python program that models and solves **Knights and Knaves** logic puzzles using **propositional logic** and **model checking**.  
In these puzzles, each character is either a Knight (always tells the truth) or a Knave (always lies).  
The program constructs logical expressions representing each puzzle (knowledge base)nand uses inference to determine who is a Knight or Knave.

---

### **Key CS/AI Concepts**
- **Knowledge representation** with propositional symbols and logical connectives.  
- **Model checking** through truth-table enumeration to test logical entailment.  
- **Logical inference** to derive conclusions that hold in all satisfying models.  
- **Symbolic reasoning** and **abstraction** for building complex logic formulas.  

---

### **Example Output**
run python puzzle.py

https://github.com/user-attachments/assets/e5603789-8bc0-425c-9ed5-0d54f246c60e


Puzzles in the demonstration: \
knowledge in knowledge bases knowledge0, knowledge1, knowledge2, and knowledge3 to solve the following puzzles:

- Puzzle 0 contains a single character, A. \
A says “I am both a knight and a knave.” \

- Puzzle 1 has two characters: A and B. \
A says “We are both knaves.” \
B says nothing.

- Puzzle 2 has two characters: A and B. \ 
A says “We are the same kind.” \
B says “We are of different kinds.”

- Puzzle 3 has three characters: A, B, and C. \ 
A says either “I am a knight.” or “I am a knave.”, but you don’t know which. \
B says “A said ‘I am a knave.’” \
B then says “C is a knave.” \
C says “A is a knight.”

In each of the above puzzles, each character is either a knight or a knave. Every sentence spoken by a knight is true, and every sentence spoken by a knave is false.


Puzzle 0 \
A is Knave

Puzzle 1 \
A is a Knave \
B is a Knight

Puzzle 2 \
A is a Knave \
B is a Knight

Puzzle 3 \
A is a Knight \
B is a Knave \
C is a Knight

