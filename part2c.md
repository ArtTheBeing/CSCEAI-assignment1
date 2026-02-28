# Part 2c: tic tac toe

Implements an optimal tic-tac-toe player using the minimax algorithm in Prolog.

Minimax recursively explores all future game states. x maximizes, o minimizes. Computer vs computer always draws.

How to run: swipl -l tictactoe.pl

?- best_move([e,e,e,e,e,e,e,e,e], x, Move).
?- play.

play simulates a full computer-vs-computer game and always ends in a draw.
