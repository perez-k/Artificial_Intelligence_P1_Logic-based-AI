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
- And known trait expression for some individuals as a CSV file,

It estimates the posterior probability for each possible number of abnormal gene copies (0, 1, or 2) that each family member might carry, and whether they are likely to express the hereditary trait. \
It accounts for mutation rates and Mendelian inheritance.

The program can work for other genetic mutation-trait pairs as long as the probability data are updated accordingly in heredity.py

---

### **Key CS/AI Concepts**
- **Bayesian networks & conditional probability tables (CPTs)** for representing uncertain genetic relationships with inheritance and mutation rules
- **Inference by enumeration** (summing over hidden variables) to compute posterior probabilities  
- **Joint, marginal, and conditional probabilities** computation
- **Normalization of probability distributions**

---

## **Example Output**

`py heredity.py data/family0.csv`

>> 
<img width="814" height="659" alt="image" src="/images/2.2_Heredity/Screenshot 1 P2.2 Heredity.png" />


Interpretation for Harry: 

  Gene: \
    2: 0.0092  [Probability that Harry have 02 mutated copies of the gene] \
    1: 0.4557   [Probability that Harry have 01 mutated copies of the gene] \
    0: 0.5351   [Probability that Harry have 00 mutated copies of the gene, so 02 normal copies] 

  Trait: \
    True: 0.2665 [Probability that Harry have hearing impairment] \
    False: 0.7335   [Probability that Harry do not have hearing impairment]



`py heredity.py data/family1.csv`
>> 
<img width="811" height="654" alt="image" src="/images/2.2_Heredity/Screenshot 2 p2.2 Heredity.png" />
