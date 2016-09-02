"""
Game: 4 to 0.
Players: two.
Objective: Each player choose to subtract either 1 or 2 from the current number,
starting at 4, before passing the new number onto the other player. The player
that *receives* the number 0 from the last player loses.

initial_position(): the initial starting position of the game.
primitive(pos): checks whether the current game is finished or still undecided.
gen_moves(pos): generates the possible set of moves available at the current state.
do_moves(pos, move): generates the position given a move from the current position.
"""

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
