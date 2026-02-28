my_intersection([], _, []).
my_intersection([H|T], L2, [H|Result]) :-
    member(H, L2), !,
    my_intersection(T, L2, Result).
my_intersection([_|T], L2, Result) :-
    my_intersection(T, L2, Result).

remdups([], []).
remdups([H|T], Result) :-
    member(H, T), !,
    remdups(T, Result).
remdups([H|T], [H|Result]) :-
    remdups(T, Result).

divisible(N, X) :-
    M is N mod X, M =:= 0.

smallest_factor(N, F, N) :- F * F > N, !.
smallest_factor(N, F, F) :- divisible(N, F), !.
smallest_factor(N, F, SF) :- F1 is F + 1, smallest_factor(N, F1, SF).

factor(1, []) :- !.
factor(N, Factors) :-
    N > 1,
    smallest_factor(N, 2, F),
    N1 is N // F,
    factor(N1, Rest),
    append(Rest, [F], Factors).

my_sqrt(N, Sqrt) :-
    my_sqrt(N, 1.0, Sqrt).

my_sqrt(N, Guess, Sqrt) :-
    Next is (Guess + N/Guess) / 2,
    Diff is abs(Next - Guess),
    ( Diff < 0.001
    -> Sqrt = Next
    ; my_sqrt(N, Next, Sqrt)
    ).


