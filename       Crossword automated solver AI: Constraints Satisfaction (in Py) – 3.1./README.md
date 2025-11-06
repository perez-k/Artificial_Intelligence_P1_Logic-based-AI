
## **Crossword AI** – CS50 AI (Constraint Satisfaction)

---

### **Description**
A Python AI program that automatically fills a crossword puzzle by modeling the problem as a **Constraint Satisfaction Problem (CSP)**.  
Each empty slot in the crossword is treated as a **variable**, and its **domain** of possible values is words from a given dictionary that fit the slot’s length.  
The solver enforces **node consistency** (word length matches slot length) and **arc consistency** (letters crossing at intersections must match). Through **constraint propagation** and **backtracking search** with heuristics, the program efficiently fills the grid with valid, intersecting words that satisfy all crossword rules. 

This approach mimics how a human might logically eliminate impossible words, then match possible word to complete the crossword.

---

### **Key CS/AI Concepts**
- **Constraint Satisfaction Problems (CSPs)**: variables, domains, constraints  
- **Consistency enforcement**: node consistency and arc consistency  
- **Search algorithms**: **backtracking** with pruning  

---

### **Example Output**
The AI can handle both simple and very complex crosswords. The program only needs the crossword structure and the dictionary.

`py generate.py data/structure2.txt data/words2.txt output2.png `

>> 
<img width="614" height="459" alt="image" src="/images/3.1_Crossword/Screenshot p3.1.png" />


`py generate.py data/structure2.txt data/words1.txt output1.png `

>> 
<img width="814" height="659" alt="image" src="/images/3.1_Crossword/img crossword.png" />




---

