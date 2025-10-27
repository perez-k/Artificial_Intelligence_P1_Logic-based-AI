# **PageRank: Probabilistic webpage ranking using Markov Chain** 

---

## **Description**
A Python implementation of the **PageRank** algorithm, used by Google search to rank web pages by importance in the search engine result. It computes the **importance of web pages** based on how likely a random web user is to land on each page. 
 
Heuristic: An “important” page is one that many other important websites link to, since it’s reasonable to imagine that more sites will link to a higher-quality webpage than a lower-quality webpage. Each page is assigned a rank based on the number of incoming links from other pages, and higher ranks indicate greater importance.

PageRank was created by Google’s co-founders (including Larry Page, for whom the algorithm was named).

To estimate page importance:

1. **Random Surfer Model** – Simulates a user clicking links at random to estimate the probability of landing on each page.
It functions as a **Markov Chain** where each page represents a state, and a transition model randomly selects one of the links on that page.
At each step, the state switches to one of the pages linked to the current one.


By randomly sampling states from the Markov Chain, we estimate each page’s PageRank. We begin by selecting a page at random and then follow links at random, tracking how many times we visit each page. After collecting all our samples — based on a number we determine beforehand — the proportion of visits to each page contributes to the estimate of that page’s rank.

To ensure we can always reach all pages that may not be linked in the corpus of web pages, the algorithm uses a damping factor d. With probability d (where d is usually set around 0.85), the random surfer will choose one of the links on the current page at random. Otherwise (with probability 1 - d), the random surfer chooses one of all the pages in the corpus at random, including the one they are currently on.

Our random surfer begins by selecting a page at random. Then, for each additional sample we want to generate, it randomly follows a link from the current page with probability d, or it picks any page at random with probability 1 - d. By tracking how often each page appears as a sample, we can consider the proportion of times a page is chosen as its PageRank.


2. **Iterative PageRank Computation** – Repeatedly updates rank values in a directed graph until they converge to stable probabilities.

Consider each possible page i that links to page p. \
For each of those incoming pages, NumLinks(i) is the number of links on page i. Each page i that links to p has its own PageRank, PR(i), which represents the probability that we are on page i at any given moment. Since we travel from page i to any of its links with equal likelihood, we divide PR(i) by NumLinks(i) to find the probability that we were on page i and selected the link to page p.

This gives us the following definition of PageRank for page p.

### PageRank Formula
$PR(p) = \frac{1 - d}{N} + d \sum_i \frac{PR(i)}{NumLinks(i)}$



The program takes a collection of HTML pages, constructs a directed hyperlink network graph of links between them, and calculates a ranking score for each page based on a probability distribution over pages that reflects their relative influence.



---

## **Key CS/AI Concepts**
- **Directed graph representation** of hyperlink networks.  
- **Markov chains** and **state transition probabilities**.  
- **Random Surfer Model** to approximate steady-state distribution.  
- **Iterative convergence algorithms** for PageRank computation.  
- **Stochastic processes** and probability distributions.  

## **Example Output**

<img width="614" height="459" alt="image" src="/images/2.1_PageRank/Screenshot 1 P2.1 PageRank.png" />

<img width="611" height="454" alt="image" src="/images/2.1_PageRank/Screenshot 2 p2.1 PageRank.png" />

<img width="609" height="448" alt="image" src="/images/2.1_PageRank/Screenshot 3 p2.1 PageRank.png" />
