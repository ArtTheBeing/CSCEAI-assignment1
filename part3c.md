# Part 3c: Peg Solitaire in CLIPS

Implements a simple linear peg solitaire player using CLIPS production rules.

The board has 9 positions (8 pegs 1 blank). The starting state is: O O O O _ O O O O, where O is a peg and _ is an empty hole. A peg can jump over an adjacent peg into the empty hole beyond it; the jumped peg is removed. Play continues until no valid moves remain.

pegsolitaire.fct defines the initial board as a set of peg and empty facts, plus a phase fact to control rule execution.

how to run:

Start CLIPS, then:
    user part 3a start
    (load "pegsolitaire.clp")
    (load-facts "pegsolitaire.fct")
    (run)
