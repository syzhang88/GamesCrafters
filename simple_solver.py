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

#4 - 0 API

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
    empty = []

    def __init__(self, position, parent = None, branches = empty):
        assert isinstance(position, int)
        assert isinstance(parent, gameTree) or parent == None
        for b in branches:
            assert isinstance(b, gameTree)
        self.position = position
        self.parent = parent
        self.branches = branches
        self.status = "Undecided"

    # def __repr__(self):
    #     return 'g'

    def getPosition(self):
        return self.position

    def getParent(self):
        return self.parent

    def getBranches(self):
        return self.branches

    def getStatus(self):
        return self.status

    def newStatus(self, s):
        # print(self.parent)
        assert s == "Loss" or s == "Win" or "Undecided" or "Tie"
        self.status = s
        currParent = self.parent
        while currParent:
            currStatus = "Loss"
            for b in currParent.getBranches():
                if b.getStatus() == "Loss":
                    currStatus = "Win"
                if b.getStatus() == "Undecided":
                    return
            currParent.newStatus(currStatus)
            currParent =  currParent.getParent()

    def newBranch(self, b):
        assert isinstance(b, gameTree)
        self.branches += [b]

    def newBranches(self, branches = []):
        for b in branches:
            assert isinstance(b, gameTree)
        self.branches = branches

    def is_leaf(self):
        return not self.branches

def simple_solver(init, prim, gen, do):
    """Returns whether or not the current player is in a winning
    initial position, with the given game parameters.
    """
    root = gameTree(init())

    currMoves = [root]
    i = 0
    while i < len(currMoves) and i < 20:
        node = currMoves[i]
        pos = node.getPosition()
        if prim(pos):
            node.newStatus("Loss")
        node.newBranches([gameTree(do(pos, move), node) for move in gen(pos)])
        currMoves = currMoves + node.getBranches()
        i += 1

    return root.status

print(simple_solver(initial_position, primitive, gen_moves, do_moves))
