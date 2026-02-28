# Part 3a: Simpsons Family Relationships in CLIPS

Uses CLIPS forward-chaining rules to infer family relationships from a base set of facts about Simpsons characters.

simpsons.fct contains the base facts: which characters are male or female, and who is a parent of whom.

How to run:

Start CLIPS, then:
    "/Applications/CLIPS IDE.app/Contents/MacOS/CLIPS IDE" << EOF
    (load "simpsons.clp")
    (load-facts "simpsons.fct")
    (run)
    EOF