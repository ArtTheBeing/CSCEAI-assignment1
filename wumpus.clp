(defrule infer-breezy-left
    (pit ?pr ?pc)
    (room ?r ?c)
    (test (= ?r ?pr))
    (test (= ?c (- ?pc 1)))
    (not (breezy ?r ?c))
    =>
    (assert (breezy ?r ?c)))

(defrule infer-breezy-right
    (pit ?pr ?pc)
    (room ?r ?c)
    (test (= ?r ?pr))
    (test (= ?c (+ ?pc 1)))
    (not (breezy ?r ?c))
    =>
    (assert (breezy ?r ?c)))

(defrule infer-breezy-above
    (pit ?pr ?pc)
    (room ?r ?c)
    (test (= ?c ?pc))
    (test (= ?r (- ?pr 1)))
    (not (breezy ?r ?c))
    =>
    (assert (breezy ?r ?c)))

(defrule infer-breezy-below
    (pit ?pr ?pc)
    (room ?r ?c)
    (test (= ?c ?pc))
    (test (= ?r (+ ?pr 1)))
    (not (breezy ?r ?c))
    =>
    (assert (breezy ?r ?c)))

(defrule infer-stenchy-left
    (wumpus ?wr ?wc)
    (room ?r ?c)
    (test (= ?r ?wr))
    (test (= ?c (- ?wc 1)))
    (not (stenchy ?r ?c))
    =>
    (assert (stenchy ?r ?c)))

(defrule infer-stenchy-right
    (wumpus ?wr ?wc)
    (room ?r ?c)
    (test (= ?r ?wr))
    (test (= ?c (+ ?wc 1)))
    (not (stenchy ?r ?c))
    =>
    (assert (stenchy ?r ?c)))

(defrule infer-stenchy-above
    (wumpus ?wr ?wc)
    (room ?r ?c)
    (test (= ?c ?wc))
    (test (= ?r (- ?wr 1)))
    (not (stenchy ?r ?c))
    =>
    (assert (stenchy ?r ?c)))

(defrule infer-stenchy-below
    (wumpus ?wr ?wc)
    (room ?r ?c)
    (test (= ?c ?wc))
    (test (= ?r (+ ?wr 1)))
    (not (stenchy ?r ?c))
    =>
    (assert (stenchy ?r ?c)))

(defrule mark-dangerous-pit
    (pit ?r ?c)
    (not (dangerous ?r ?c))
    =>
    (assert (dangerous ?r ?c)))

(defrule mark-dangerous-wumpus
    (wumpus ?r ?c)
    (not (dangerous ?r ?c))
    =>
    (assert (dangerous ?r ?c)))

(defrule mark-dangerous-stenchy
    (stenchy ?r ?c)
    (not (dangerous ?r ?c))
    =>
    (assert (dangerous ?r ?c)))

(defrule mark-safe
    (room ?r ?c)
    (not (dangerous ?r ?c))
    (not (safe ?r ?c))
    =>
    (assert (safe ?r ?c))
    (printout t "safe: (" ?r "," ?c ")" crlf))

(defrule start-reachable
    (safe 1 1)
    (not (reachable 1 1))
    =>
    (assert (reachable 1 1))
    (printout t "reachable: (1,1)  [start]" crlf))

(defrule reach-adjacent
    (reachable ?r ?c)
    (safe ?r2 ?c2)
    (test (or (and (= ?r2 ?r) (= (abs (- ?c2 ?c)) 1))
              (and (= ?c2 ?c) (= (abs (- ?r2 ?r)) 1))))
    (not (reachable ?r2 ?c2))
    =>
    (assert (reachable ?r2 ?c2))
    (printout t "reachable: (" ?r2 "," ?c2 ")" crlf))

(defrule path-found
    (reachable 4 3)
    =>
    (printout t "A safe path to (4,3) exists." crlf))


(defrule no-path
    (not (reachable 4 3))
    =>
    (printout t crlf)
    (printout t "==> No safe path from (1,1) to (4,3) found." crlf))
