# Part 1b: Vertex Cover

Encodes the minimum vertex cover problem as SAT and solves it.

A vertex cover of a graph is a set of vertices such that every edge has at least one endpoint in the set. The problem asks for the smallest such set.

vertex_cover.py takes the graph defined in the 4clique.pptx slides, encodes the vertex cover constraints as CNF clauses, and calls the SAT solver to find a valid cover. It tries increasing cover sizes until a satisfiable one is found.

How to run: python3 vertex_cover.py