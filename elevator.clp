(defrule serve-request
    (declare (salience 100))
    ?req <- (request ?f)
    (elevator-floor ?f)
    =>
    (retract ?req)
    (printout t "floor " ?f " -- doors open, passenger served." crlf))

(defrule start-moving-up
    ?dir <- (elevator-direction idle)
    (elevator-floor ?f)
    (request ?above&:(> ?above ?f))
    =>
    (retract ?dir)
    (assert (elevator-direction up))
    (printout t "starting upward from floor " ?f crlf))

(defrule start-moving-down
    ?dir <- (elevator-direction idle)
    (elevator-floor ?f)
    (not (request ?above&:(> ?above ?f)))
    (request ?below&:(< ?below ?f))
    =>
    (retract ?dir)
    (assert (elevator-direction down))
    (printout t "starting downward from floor " ?f crlf))

(defrule go-idle-up
    ?dir <- (elevator-direction up)
    (not (request ?))
    =>
    (retract ?dir)
    (assert (elevator-direction idle)))

(defrule go-idle-down
    ?dir <- (elevator-direction down)
    (not (request ?))
    =>
    (retract ?dir)
    (assert (elevator-direction idle)))


(defrule done
    (declare (salience -1))
    (elevator-direction idle)
    (elevator-floor ?f)
    (not (request ?))
    =>
    (printout t crlf "==> All requests served. Elevator resting at floor " ?f "." crlf))
