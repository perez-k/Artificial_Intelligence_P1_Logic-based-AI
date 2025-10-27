# **Heredity: Genetic as a Bayesian Network** 

---

## **Description**
A Python program that models inheritance of the **GJB2 gene (Connexin 26)** and the expression of **congenital hearing impairment** using a **Bayesian network**. 
Each person can have **0, 1, or 2 copies** of the mutated GJB2 allele; parents pass one copy to each child with a **1% mutation probability** (flip to/from the target allele). 
Trait likelihood depends on gene copies:
- **0 copies → ~1%** chance of trait  
- **1 copy → ~56%** chance of trait  
- **2 copies → ~65%** chance of trait  

Given:
- A family tree (parents/children),
- And known trait expression for some individuals as a csv file,
It estimates the posterior probability for each possible number of abnormal gene copies (0, 1, or 2) that each family member might carry, and whether they are likely to express the hereditary trait.  
It accounts for mutation rates and Mendelian inheritance.



---

### **Key CS/AI Concepts**
- **Bayesian networks & conditional probability tables (CPTs)** for representing uncertain genetic relationships with inheritance and mutation rules
- **Inference by enumeration** (summing over hidden variables) to compute posterior probabilities  
- **Joint, marginal, and conditional probabilities** computation
- **Normalization of probability distributions**

---

## **Example Output**

