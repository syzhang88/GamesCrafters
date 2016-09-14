"""
***Updates to be added after 9/12/16***
- memoization with table (added 9/14/16)
- invalid input checker
- draw checker
- tie primitive

Game: 4 to 0.
Players: two.
Objective: each player choose to subtract either 1 or 2 from the current number,
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
    memo = {}
    empty = []

    def __init__(self, position, parent = None, branches = empty):
        assert isinstance(position, int)
        assert isinstance(parent, gameTree) or parent == None
        for b in branches:
            assert isinstance(b, gameTree)
        self.position = position
        self.parent = parent
        self.branches = branches

    def getPosition(self):
        return self.position

    def getParent(self):
        return self.parent

    def getBranches(self):
        return self.branches

    def getStatus(self):
        if not gameTree.memo.get(self.position):
            status = "Loss"
            for branch in self.branches:
                if not gameTree.memo.get(branch.position):
                    branch.getStatus()
                if gameTree.memo[branch.position] == "Loss":
                    status = "Win"
                elif gameTree.memo[branch.position] == "Tie":
                    status = "Tie"
                elif gameTree.memo[branch.position] == "Undecided":
                    status = "Undecided"
            self.newStatus(status)
        return gameTree.memo[self.position]

    def newStatus(self, s):
        assert s == "Loss" or s == "Win" or s == "Undecided" or s == "Tie" or s == "Draw"
        gameTree.memo[self.position] = s
        # self.status = s
        # currParent = self.parent
        # while currParent:
        #     currStatus = "Loss"
        #     for b in currParent.getBranches():
        #         if b.getStatus() == "Loss":
        #             currStatus = "Win"
        #             break
        #         if b.getStatus() == "Undecided":
        #             return
        #     currParent.newStatus(currStatus)
        #     currParent =  currParent.getParent()

    def newBranch(self, b):
        assert isinstance(b, gameTree)
        self.branches += [b]

    def newBranches(self, branches = []):
        for b in branches:
            assert isinstance(b, gameTree)
        self.branches = branches

    def is_leaf(self):
        return not self.branches

#Simple Solver

def simple_solver(init, prim, gen, do):
    """Returns whether or not the current player is in a winning
    initial position, with the given game parameters.
    """
    root = gameTree(init())

    currMoves = [root]
    i = 0
    while i < len(currMoves):
        node = currMoves[i]
        pos = node.getPosition()
        if prim(pos):
            node.newStatus("Loss")
        node.newBranches([gameTree(do(pos, move), node) for move in gen(pos)])
        currMoves = currMoves + node.getBranches()
        i += 1

    return root.getStatus()

print(simple_solver(initial_position, primitive, gen_moves, do_moves))
