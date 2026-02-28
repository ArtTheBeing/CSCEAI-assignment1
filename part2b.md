# Part 2b: Solving a CSP in Prolog

csp.pl

Australia map coloring: assigns one of four colors (red, green, blue, yellow) to six regions (WA, NT, SA, Q, NSW, VIC) such that no two adjacent regions share a color.

SEND + MORE = MONEY: each letter maps to a unique digit 0-9, with no leading zeros, satisfying the arithmetic equation.

clpr.pl

Uses clp(r) to solve a system of simultaneous linear equations and a mortgage calculation. Constraints are declared symbolically and the solver returns numeric results.

How to run: swipl -l csp.pl

?- australia(WA, NT, SA, Q, NSW, VIC).
?- send_more_money(S, E, N, D, M, O, R, Y).
?- all_colorings.

For clpr.pl: swipl -l clpr.pl

?- testcase(X, Y, Z).
?- mg(1000, 10, 150, 10/100, B).

