
# Degrees – CS50 AI (Search)
- Actor Connection Degrees: Shortest Path Breadth-first search

---

## Description  
A Python program that determines the shortest path between two actors by linking them through the movies they have appeared in together.  \
Uses data from the IMDb database (provided in CSV format) and models the problem as a graph, where actors are connected via shared movies. \
It is a search problem where the **states** are people, the **actions** are movies, which take us from one actor to another. Our initial state and goal state are defined by the two people we’re trying to connect. By using **breadth-first search**, we can find the shortest path from one actor to another. \
The output is the smallest number of connections, "degrees of separation" between the two chosen actors.


---

### **Key CS/AI Concepts**
- **Graph representation**: actors as nodes, shared movies as edges.  
- **Breadth-First Search (BFS)** for shortest path in an unweighted graph.  
**Queue-based frontier** for systematic exploration of neighbors.  
- **Optimization of search algorithms** to guarantee the minimal connection path.
- **Data parsing** and preprocessing from CSV into Python dictionaries.  


---

### **Example Output**

My Video:

https://github.com/user-attachments/assets/e296b38d-85c7-4aaf-925d-7f88869334ab

Sample:
```
$ python degrees.py large
Loading data...
Data loaded.
Name: Mandy Patinkin
Name: Tom Cruise
4 degrees of separation.
1: Mandy Patinkin and Robin Wright starred in The Princess Bride
2: Robin Wright and Gary Sinise starred in Forrest Gump
3: Gary Sinise and Kevin Bacon starred in Apollo 13
4: Kevin Bacon and Tom Cruise starred in A Few Good Men
---







