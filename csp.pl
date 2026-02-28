:- use_module(library(clpfd)).

color(red).
color(green).
color(blue).
color(yellow).

australia(WA, NT, SA, Q, NSW, VIC) :-
    color(WA), color(NT), color(SA),
    color(Q), color(NSW), color(VIC),
    WA \= NT, WA \= SA,
    NT \= SA, NT \= Q,
    SA \= Q, SA \= NSW, SA \= VIC,
    Q \= NSW,
    NSW \= VIC.

all_colorings :-
    australia(WA, NT, SA, Q, NSW, VIC),
    format("WA=~w  NT=~w  SA=~w  Q=~w  NSW=~w  VIC=~w~n", [WA, NT, SA, Q, NSW, VIC]),
    fail.
all_colorings.

count_colorings(N) :-
    findall(_, australia(_, _, _, _, _, _), Sols),
    length(Sols, N).

send_more_money(S,E,N,D,M,O,R,Y) :-
    Vars = [S,E,N,D,M,O,R,Y],
    Vars ins 0..9,
    S #\=0,
    M #\=0,
    all_different(Vars), S*1000 + E*100 + N*10 + D + M*1000 + O*100 + R*10 + E #= M*10000 + O*1000 + N*100 + E*10 + Y,
    label(Vars).

