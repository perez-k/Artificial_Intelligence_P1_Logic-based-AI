## **PageRank: Probabilistic webpage ranking** 

---

### **Description**
A Python implementation of the **PageRank** algorithm, used by Google search to rank web pages by importance in the search engine result. It computes the **importance of web pages** based on how likely a random web user is to land on each page.  
Heuristic: An “important” page is one that many other important websites link to, since it’s reasonable to imagine that more sites will link to a higher-quality webpage than a lower-quality webpage. each page is given a rank according to the number of incoming links it has from other pages, and higher ranks would signal higher importance.
PageRank was created by Google’s co-founders (including Larry Page, for whom the algorithm was named).

To estimate page importance:

1. **Random Surfer Model** – Simulates a user clicking links at random to estimate the probability of landing on each page.
It works as a Markov Chain, where each page represents a state, and each page has a transition model that chooses among its links at random. At each time step, the state switches to one of the pages linked to by the current state.

By sampling states randomly from the Markov Chain, we get an estimate for each page’s PageRank. We start by choosing a page at random, then keep following links at random, keeping track of how many times we’ve visited each page. After we’ve gathered all of our samples (based on a number we choose in advance), the proportion of the time we were on each page contribute to the estimate for that page’s rank.

To ensure we can always get to all pages that may not be linked in the corpus of web pages, the algorithm use a damping factor d. With probability d (where d is usually set around 0.85), the random surfer will choose from one of the links on the current page at random. But otherwise (with probability 1 - d), the random surfer chooses one out of all of the pages in the corpus at random (including the one they are currently on).

Our random surfer now starts by choosing a page at random, and then, for each additional sample we’d like to generate, chooses a link from the current page at random with probability d, and chooses any page at random with probability 1 - d. If we keep track of how many times each page has shown up as a sample, we can treat the proportion of states that were on a given page as its PageRank.

2. **Iterative PageRank Computation** – Repeatedly updates rank values in a directed graph until they converge to stable probabilities.

For the second condition, we need to consider each possible page i that links to page p. For each of those incoming pages, let NumLinks(i) be the number of links on page i. Each page i that links to p has its own PageRank, PR(i), representing the probability that we are on page i at any given time. And since from page i we travel to any of that page’s links with equal probability, we divide PR(i) by the number of links NumLinks(i) to get the probability that we were on page i and chose the link to page p.

This gives us the following definition for the PageRank for a page p.

The program takes a collection of HTML pages, builds a directed **hyperlink network graph** of links between them, and computes a ranking score for each page based on probability distribution over pages representing their relative influence.



---

### **Key CS/AI Concepts**
- **Directed graph representation** of hyperlink networks.  
- **Markov chains** and **state transition probabilities**.  
- **Random Surfer Model** to approximate steady-state distribution.  
- **Iterative convergence algorithms** for PageRank computation.  
- **Stochastic processes** and probability distributions.  

---
- **Directed graph representation** of hyperlink structures  
- **Markov chains** and **transition probability matrices**  
- **Stochastic processes** and equilibrium (steady-state) distributions  
- **Iterative convergence algorithms** for fixed-point approximation  
- **Uncertainty modeling** through probability distributions  

### **Example Output**

