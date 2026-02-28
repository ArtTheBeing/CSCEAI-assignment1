# Part 3b: Wumpus World in CLIPS

Uses CLIPS rules to reason about a 4x4 Wumpus World grid, then determines whether a safe path exists from room (1,1) to room (4,3).

wumpus.fct defines the grid rooms, pit locations, and the wumpus location. The layout used is: pits at (3,1), (3,3), and (4,4); wumpus at (1,3).

How to run:

Start CLIPS, then:
    use part 3a start
    (load "wumpus.clp")
    (load-facts "wumpus.fct")
    (run)
