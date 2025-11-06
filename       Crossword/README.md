
## **Crossword AI** – CS50 AI (Constraint Satisfaction)

---

### **Description**
A Python program that automatically fills a crossword puzzle using a **Constraint Satisfaction Problem (CSP)** formulation.  
Words are variables; each variable’s domain is all dictionary entries of the correct length.  
The solver enforces **node consistency** (length), **arc consistency** (crossing letters must match), and uses **backtracking search** with heuristics to find a complete, consistent assignment.

---

### **Key CS/AI Concepts**
- **Constraint Satisfaction Problems (CSPs)**: variables, domains, constraints  
- **Consistency enforcement**: node consistency and **AC-3** for arc consistency  
- **Search algorithms**: **backtracking** with pruning  
- **Variable ordering heuristics**: **MRV (Minimum Remaining Values)**, **Degree heuristic**  
- **Value ordering heuristic**: **Least-Constraining Value (LCV)**  
- **Problem decomposition & constraint propagation** for efficiency

---

### **Example Output**
