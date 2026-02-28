# Part 1a: 8-Queen

Encodes the 8-queens problem as a propositional satisfiability problem and solves it using a SAT solver.

The 8-queens problem asks: place 8 queens on an 8x8 chessboard so that no two queens share a row, column, or diagonal.

queens.py generates the CNF clauses encoding these constraints, then passes them to the SAT solver to find solutions. It finds at least 2 distinct solutions.

How to run: python3 queens.py

