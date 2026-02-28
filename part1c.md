# Part 1c: k-Clique

Encodes the k-clique problem as SAT and solves it.

A k-clique is a set of k vertices in a graph where every pair of vertices is connected by an edge. Given a graph and a value k, the problem asks whether such a clique exists.

kclique.py takes the graph from the 4clique.pptx slides, encodes the clique constraints as CNF clauses, and calls the SAT solver to determine whether a k-clique exists. It tries different values of k and reports the result.

How to run: python3 kclique.py

