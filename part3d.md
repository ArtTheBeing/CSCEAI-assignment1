# Part 3d: Elevator Simulator in CLIPS (Unfinished)

Simulates a 5-floor elevator controller using CLIPS production rules.

elevator.fct defines the initial state: the elevator starts at floor 1 with direction idle, and there are pending requests for floors 3, 5, 2, and 4.

How to run:

Start CLIPS, then:
    use part 3a start
    (load "elevator.clp")
    (load-facts "elevator.fct")
    (run)
