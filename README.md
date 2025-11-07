# Projects_CS50_Artificial_Intelligence (Part 1: Logic Based AI)
Projects in **Python** \
**CS50AI 2020 PSets solutions - (HarvardX, Completed in Fall 2020)**


## Overview
This repository contains my [HarvardX's CS50AI 2020](https://cs50.harvard.edu/ai/2020/) programming projects. 

## Contents
- `Search Problems`: [Degrees: Shortest path Search (in Python)](/Degrees:%20Shortest%20path%20Search%20(in%20Py)%20–%200.1./); [Tic Tac Toe: Minimax AI Player (in Python)](/%20Tic%20Tac%20Toe:%20Minimax%20AI%20Player%20(in%20Py)%20–%200.2./)
- `Knowledge representation and inference Problems`: [Knights and Knaves Logic Solver (in Python)](/%20%20Knights%20and%20Knaves%20Logic%20Solver%20(in%20Py)%20–%201.1./); [Minesweeper Inference Engine (in Python)](/%20%20%20Minesweeper%20Inference%20Engine%20(in%20Py)%20–%201.2./)
- `Uncertainty (probability)`: [PageRank: Probabilistic Web Page Ranking with Markov Chain (in Python)](/%20%20%20%20PageRank:%20Probabilistic%20Web%20Page%20Ranking%20(in%20Py)%20–%202.1./); [Heredity: Genetic as a Bayesian Network (in Python)](/%20%20%20%20%20Heredity:%20Genetic%20as%20a%20Bayesian%20Network%20(in%20Py)%20–%202.2./)
- `Optimization`: [Crossword automated solver AI: Constraints Satisfaction (in Python)](/%20%20%20%20%20%20Crossword%20automated%20solver%20AI%3A%20Constraints%20Satisfaction%20(in%20Py)%20–%203.1./)
<!--
- `pset6`: [Mario Pyramid generator (in Python)](/%20Mario%20Pyramid%20generator%20(in%20Python)%20–%206.2./); [Cash Coin change (in Python)](/%20%20Cash%20Coin%20change%20(in%20Python)%20–%20%206.3./); [Readability Level estimator (in Python)](/%20%20%20Readability%20Level%20estimator%20(in%20Python)%20–%20%206.4./); [DNA Profiling (in Python)](/%20%20%20%20DNA%20Profiling%20(in%20Python)%20–%206.5./)
- `pset7`: [Movie Database querying (in SQL)](/%20%20%20%20%20Movie%20Database%20querying%20(in%20SQL)%20–%207.1./); [Hogwarts House queries (in Py and SQL)](/%20%20%20%20%20%20Hogwarts%20House%20queries%20(in%20Py%20and%20SQL)%20–%207.2./)
- `pset8`: Homepage Basic website (in HTML, CSS, and JavaScript)
Website with Flask and JavaScript (Web)
- `final_project`: [Project Name/Description]
-->x

## Topics covered
📚 Topics Covered include:

0. Search \
[Lecture notes](https://cs50.harvard.edu/ai/2020/notes/0/), [Files](https://cs50.harvard.edu/ai/2020/weeks/0/) \
Finding a solution to a problem, like a navigator app that finds the best route from your origin to the destination, or like playing a game and figuring out the next move. \
Uninformed search (Depth-First Search, Breadth-First Search) -  Informed search (Greedy Best-First Search [use heuristic function], A* Search [use heuristic and cost estimation]) - Adversarial search (Minimax, Alpha-Beta Pruning, Depth-Limited Minimax)

1. Knowledge \
[Lecture notes](https://cs50.harvard.edu/ai/2020/notes/1/), [Files](https://cs50.harvard.edu/ai/2020/weeks/1/) \
Representing information and drawing inferences from it. (Knowledge-Based Agent)\
Inference: determine if KB ⊨ α [does KB entails α?] (in other words, answering the question: “can we conclude that α is true based on our knowledge base”) \
Propositional Logic with logical connector: [not(¬P); and(P ∧ Q); inclusive or(P ∨ Q); exclusive or(P ⊕ Q); implication(P → Q); biconditional(P ↔ Q)] \
First Order Logic: more succinct with Constant Symbols (objects) and Predicate Symbols (relations)

2. Uncertainty \
[Lecture notes](https://cs50.harvard.edu/ai/2020/notes/2/), [Files](https://cs50.harvard.edu/ai/2020/weeks/2/) \
Dealing with uncertain events using probability to create AI that makes optimal decisions given limited information and uncertainty.
Probability: 0 < P(ω) < 1; $\sum_{\omega \in \Omega} P(\omega) = 1$ \
Conditional Probability:  P(a | b) [probability of a given b] $P(a \mid b) = \dfrac{P(a \land b)}{P(b)}$ \
Random variable: Eg Roll, fair dice that can take on the values {0, 1, 2, 3, 4, 5, 6}.  Eg Flight P(Flight = on time) = 0.6, P(Flight = delayed) = 0.3, P(Flight = canceled) = 0.1  | Probability distribution can be represented more succinctly as a vector. For example, P(Flight) = <0.6, 0.3, 0.1>. \
Independance: P(a ∧ b) = P(a)P(b). \
Bayes’ Rule: $P(a \mid b) = \dfrac{P(a)\. P(b \mid a)}{P(b)}$ \
Other Probability Rules: Negation: P(¬a) = 1 - P(a);  Inclusion-Exclusion: P(a ∨ b) = P(a) + P(b) - P(a ∧ b);  Marginalization: P(a) = P(a, b) + P(a, ¬b);  Conditioning: P(a) = P(a | b)P(b) + P(a | ¬b)P(¬b) \
Bayesian network: data structure that represents the dependencies among random variables

- Inference by Enumeration: finding the probability distribution of variable X given observed evidence e and some hidden variables Y. $P(X \mid e) = \alpha\, P(X, e) = \alpha \sum_y P(X, e, y)$ | Many Python libraries (pomogranate)
Sometimes Sampling to approximate inference (Large or complex models, continuous variables, ...)

- Markov Models
based on Markov assumption: assumption that the current state depends on only a finite fixed number of previous states.
Markov chain: a sequence of random variables where the distribution of each variable follows the Markov assumption. That is, each event in the chain occurs based on the probability of the event before it.



3. Optimization \
[Lecture notes](https://cs50.harvard.edu/ai/2020/notes/3/), [Files](https://cs50.harvard.edu/ai/2020/weeks/3/) \
Choosing the best option from a set of possible options.  Finding not only a correct way to solve a problem, but a better—or the best—way to solve it. 

Local search: search algorithm that maintains a single node and searches by moving to a neighboring node minimizing or maximizing cost. (different from previous mentioned types of search). Most applicable when really don't care about the path at all, and all care about is what the solution is. Often bring to an answer that is not optimal but “good enough,” conserving computational power. Eg: 04 houses in set locations. We want to build two hospitals, such that we minimize the distance from each house to a hospital.
- Hill climbing (one type of a local search algorithm). In this algorithm, the neighbor states are compared to the current state, and if any of them is better, change the current node from the current state to that neighbor state. Risk of getting stuck in a local maximum (or minimum). | Variants (Steepest-ascent, Stochastic, First-choice, Random-restart, Local Beam Search)
- Simulated Annealing: starts with a "high temperature", being more likely to make random decisions, and, as the "temperature" decreases, it becomes less likely to make random decisions, becoming more “firm.” This mechanism allows the algorithm to change its state to a neighbor that’s worse than the current state to escape from local maxima and increase probability of finding global maximum.

Linear Programming
Problems that optimize a linear equation (an equation of the form y = ax₁ + bx₂ + …) with constraints attached (a₁x₁ + a₂x₂ + … + aₙxₙ ≤ b). Simplex and Interior-Point \
Eg: optimize productions, and costs


Constraints satisfaction problem: Backtracking Search \
Eg: In sudoku, or to schedule exams for a university giving students availability constraints (students cannot have 02 exams at the same time)


in Part 2

5. Learning \
Improving performance based on access to data and experience. For example, your email is able to distinguish spam from non-spam mail based on past experience.

6. Neural Networks \
A program structure inspired by the human brain that is able to perform tasks effectively.

7. Language \
Processing natural language, which is produced and understood by humans.







## Certificate
![CS50x Certificate](images/Certificat_CS50AI.png)

