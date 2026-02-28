(defrule find-move-right
    (phase find-moves)
    (peg ?from)
    (peg ?via&:(= ?via (+ ?from 1)))
    (empty ?to&:(= ?to (+ ?from 2)))
    =>
    (assert (move ?from ?via ?to))
    (printout t ?from " -> " ?to " (over "?via")" crlf))

(defrule find-move-left
    (phase find-moves)
    (peg ?from)
    (peg ?via&:(= ?via (- ?from 1)))
    (empty ?to&:(= ?to (- ?from 2)))
    =>
    (assert (move ?from ?via ?to))
    (printout t ?from " -> " ?to " (over "?via")" crlf))

(defrule moves-found
    (declare (salience -5))
    ?phase <- (phase find-moves)
    (move ? ? ?)
    =>
    (retract ?phase)
    (assert (phase apply-move)))

(defrule no-moves-found
    (declare (salience -5))
    ?phase <- (phase find-moves)
    =>
    (retract ?phase)
    (assert (phase done)))

(defrule apply-one-move
    (declare (salience 20))
    (phase apply-move)
    ?m  <- (move ?from ?via ?to)
    ?pf <- (peg ?from)
    ?pv <- (peg ?via)
    ?et <- (empty ?to)
    =>
    (retract ?m ?pf ?pv ?et)
    (assert (applied))
    (assert (peg ?to))
    (assert (empty ?from))
    (assert (empty ?via))
    (printout t ?from " jumps over "?via" -> lands at " ?to crlf))

(defrule clear-unused-moves
    (declare (salience 10))
    (phase apply-move)
    ?m <- (move ? ? ?)
    =>
    (retract ?m))

(defrule end-apply-phase
    (declare (salience -5))
    ?phase  <- (phase apply-move)
    ?flag   <- (applied)
    =>
    (retract ?phase ?flag)
    (assert (phase find-moves))
    (printout t crlf))

(defrule count-pegs
    (declare (salience 10))
    (phase done)
    (peg ?pos)
    =>
    (printout t "Peg remaining at position" ?pos crlf))

(defrule game-over
    (declare (salience -10))
    (phase done)
    =>
    (printout t crlf "==> Game over" crlf))
