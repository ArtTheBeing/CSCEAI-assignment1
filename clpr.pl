:- use_module(library(clpr)).

testcase(X,Y,Z) :- {3*X + 4*Y - 2*Z = 8, X - 5*Y + Z = 10, 2*X + 3*Y -Z = 20}.

mg(P, T, R, I, B) :- {T = 0, B = P}.
mg(P, T, R, I, B) :- {T >= 1, P1 = P*(1+I) - R}, mg(P1, T - 1, R, I, B).

dog(fido).
dog(snoopy).
