
## **Crossword AI** – CS50 AI (Constraint Satisfaction)

---

### **Description**
A Python AI program that automatically fills a crossword puzzle by modeling the problem as a **Constraint Satisfaction Problem (CSP)**.  
Each empty slot in the crossword is treated as a **variable**, and its **domain** of possible values being words from a given dictionary that fit the slot’s length.  
The solver enforces **node consistency** (word length matches slot length), **arc consistency** (crossing letters must match at intersections). Through **constraint propagation** and **backtracking search** with heuristics, the program efficiently fills the grid with valid, intersecting words that satisfy all crossword rules. 

This approach mimics how a human might logically eliminate impossible words, then match possible word to complete the crossword.

---

### **Key CS/AI Concepts**
- **Constraint Satisfaction Problems (CSPs)**: variables, domains, constraints  
- **Consistency enforcement**: node consistency and arc consistency  
- **Search algorithms**: **backtracking** with pruning  

---

### **Example Output**







---

### **CV Bullet Points**
- Developed an **AI-based crossword solver** using a **Constraint Satisfaction Problem (CSP)** formulation.  
- Implemented **node and arc consistency** algorithms (AC-3) to prune invalid word assignments.  
- Applied **heuristic search** (MRV, Degree, LCV) and **backtracking** to efficiently generate valid crossword solutions.  
- Strengthened understanding of **AI search algorithms**, **constraint reasoning**, and **optimization in Python**.
