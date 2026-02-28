opponent(x, o).
opponent(o, x).
empty_board([e,e,e, e,e,e, e,e,e]).
replace([_|T], 1, V, [V|T]).
replace([H|T], N, V, [H|T1]) :-
    N > 1, N1 is N - 1,
    replace(T, N1, V, T1).

make_move(Board, Pos, Player, NewBoard) :-
    nth1(Pos, Board, e),
    replace(Board, Pos, Player, NewBoard).

available(Board, Moves) :-
    findall(P, nth1(P, Board, e), Moves).


win_line([1,2,3]). win_line([4,5,6]). win_line([7,8,9]).
win_line([1,4,7]). win_line([2,5,8]). win_line([3,6,9]).
win_line([1,5,9]). win_line([3,5,7]).
wins(Board, P) :-
    win_line([A,B,C]),
    nth1(A, Board, P), nth1(B, Board, P), nth1(C, Board, P).

terminal(Board, 1)  :- wins(Board, x), !.
terminal(Board, -1) :- wins(Board, o), !.
terminal(Board, 0)  :- \+ member(e, Board), !.

minimax(Board, Player, BestMove, BestScore) :-
    available(Board, Moves),
    Moves \= [],
    opponent(Player, Opp),
    minimax_moves(Board, Player, Opp, Moves, BestMove, BestScore).

minimax_moves(Board, Player, Opp, [M|Rest], BestMove, BestScore) :-
    make_move(Board, M, Player, NB),
    ( terminal(NB, S) -> Score = S
    ; minimax(NB, Opp, _, Score)
    ),
    ( Rest = []
    -> BestMove = M, BestScore = Score
    ; minimax_moves(Board, Player, Opp, Rest, BM2, BS2),
      ( Player = x, Score >= BS2 -> BestMove = M, BestScore = Score
      ; Player = o, Score =< BS2 -> BestMove = M, BestScore = Score
      ; BestMove = BM2, BestScore = BS2
      )
    ).


best_move(Board, Player, Move) :-
    minimax(Board, Player, Move, _).

print_cell(e) :- write('.').
print_cell(x) :- write(x).
print_cell(o) :- write(o).

print_row(A, B, C) :-
    print_cell(A), write('|'), print_cell(B), write('|'), print_cell(C), nl.

print_board([A,B,C, D,E,F, G,H,I]) :-
    print_row(A, B, C),
    write('-|-|-'), nl,
    print_row(D, E, F),
    write('-|-|-'), nl,
    print_row(G, H, I).


play_game(Board, _) :-
    terminal(Board, Score), !,
    nl, write('Final board:'), nl,
    print_board(Board),
    ( Score =:=  1 -> write('X winner')
    ; Score =:= -1 -> write('O winner')
    ; write('Draw')
    ), nl.
play_game(Board, Player) :-
    format("~n~w to move:~n", [Player]),
    print_board(Board),
    minimax(Board, Player, Move, Score),
    format("plays position ~w (expected score: ~w)~n", [Move, Score]),
    make_move(Board, Move, Player, NB),
    opponent(Player, Opp),
    play_game(NB, Opp).

play :-
    write('Comp vs Comp'), nl,
    empty_board(B),
    play_game(B, x).
