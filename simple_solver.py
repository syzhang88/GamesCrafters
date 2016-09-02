"""
Game: 4 to 0.
Players: 2
Objective: Each player choose to subtract either 1 or 2 from the current number,
starting at 4, before passing the new number onto the other player. The player
that *receives* the number 0 from the last player loses.

initial_position(): The initial starting position of the game.
primitive(pos): Checks whether the current game is finished or still undecided.
gen_moves(pos): Generates the possible set of moves available at the current state.
do_moves(pos, move): Generates the position given a move from the current position.
"""

#4 to 0 GamesmanAPI

def initial_position():
    return 4

def primitive(pos):
    if pos <= 0:
        return True
    return False

def gen_moves(pos):
    possible_moves = []
    if pos - 1 >= 0:
        possible_moves += [1]
    if pos - 2 >= 0:
        possible_moves += [2]
    return possible_moves

def do_moves(pos, move):
    return pos - move

#Simple Solver

def simple_solver(init, prim, gen, do):
    """Returns whether or not Player 1 can win inputted game from given initial
    position.

    >>> simple_solver(initial_position, primitive, gen_moves, do_moves)
    "Player 1 is currently at a tie." """
    current_state = [init()]
    turn = 1
    win = 0
    lose = 0
    for i in current_state:
        if prim(i):
            if turn == 1:
                lose += 1
            if turn == 2:
                win += 1
        current_state += [do(i, m) for m in gen(i)]
        turn = 3 - turn
    if win > 0 and lose > 0:
        return "Player 1 is currently at a tie."
    elif win > 0:
        return "Player 1 has won."
    else:
        return "Player 1 has lost."
