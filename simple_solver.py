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

#Game Tree

class gameTree:
    def __init__(self, position, branches = []):
        for b in branches:
            assert isinstance(b, gameNode)
        self.position = position
        self.branches = branches

    def __len__(self):
        return 1 + max([len(b) for b in self.branches])

    def __repr__(self):
        if self.rest:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'gameTree({0}{1})'.format(self.position, self.branches_str)

    def position(self):
        return self.pos
    def is_leaf(self):
        return not self.branches

#Simple Solver
def simple_solver(init, prim, gen, do):
    #generate tree with iterative loop
    #go back up tree, adding W/L: W if L for one of its branches; else, L.
    #return W/L value of root

def simple_solver(init, prim, gen, do):
    """Returns whether or not the current player can win from a given
    initial position, with the given game parameters.

    >>> simple_solver(initial_position, primitive, gen_moves, do_moves)
    "This position is currently at a tie; the player can still either lose or win." """
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
        return "This position is currently at a tie; the player can still either lose or win."
    elif win > 0:
        return "This is a winning position."
    else:
        return "This is a losing position."
