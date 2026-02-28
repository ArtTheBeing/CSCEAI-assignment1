(defrule infer-father
    (male ?p)
    (parentOf ?c ?p)
    =>
    (assert (father ?p ?c))
    (printout t "father: " ?p " is the father of " ?c crlf))

(defrule infer-mother
    (female ?p)
    (parentOf ?c ?p)
    =>
    (assert (mother ?p ?c))
    (printout t "mother: " ?p " is the mother of " ?c crlf))

(defrule infer-sibling
    (parentOf ?x ?p)
    (parentOf ?y ?p)
    (test (neq ?x ?y))
    =>
    (assert (sibling ?x ?y))
    (printout t "siblings: " ?x " and " ?y crlf))

(defrule infer-grandparent
    (parentOf ?child ?parent)
    (parentOf ?parent ?grandparent)
    =>
    (assert (grandparent ?child ?grandparent))
    (printout t "grandparent: " ?grandparent " is grandparent of " ?child crlf))

(defrule infer-grandmother
    (female ?gp)
    (grandparent ?gp ?gc)
    =>
    (assert (grandmother ?gp ?gc))
    (printout t "grandmother: " ?gp " is grandmother of " ?gc crlf))

(defrule infer-grandfather
    (male ?gp)
    (grandparent ?gp ?gc)
    =>
    (assert (grandfather ?gp ?gc))
    (printout t "grandfather: " ?gp " is grandfather of " ?gc crlf))

(defrule infer-aunt
    (female ?aunt)
    (sibling ?aunt ?parent)
    (parentOf ?child ?parent)
    =>
    (assert (aunt ?aunt ?child))
    (printout t "aunt: " ?aunt " is aunt of " ?child crlf))

(defrule infer-uncle
    (male ?uncle)
    (sibling ?uncle ?parent)
    (parentOf ?child ?parent)
    =>
    (assert (uncle ?uncle ?child))
    (printout t "uncle: " ?uncle " is uncle of " ?child crlf))

(defrule infer-cousin
    (sibling ?p1 ?p2)
    (parentOf ?c1 ?p1)
    (parentOf ?c2 ?p2)
    (test (neq ?c1 ?c2))
    =>
    (assert (cousin ?c1 ?c2))
    (printout t "cousins: " ?c1 " and " ?c2 crlf))
