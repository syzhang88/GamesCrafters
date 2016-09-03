class gameTree:
    empty = []

    def __init__(self, position, branches = empty):
        for b in branches:
            assert isinstance(b, gameNode)
        self.position = position
        self.status = "Game is undecided at current position."
        self.branches = branches

    def __len__(self):
        return 1 + max([len(b) for b in self.branches])

    def __repr__(self):
        if self.rest:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'gameTree({0}{1})'.format(self.status, self.branches_str)

    def position(self):
        return self.position

    def status(self):
        return self.status

    def branches(self):
        return self.branches

    def newStatus(self, s):
        assert isinstance(s, string)
        self.status = s

    def newBranch(self, b):
        assert isinstance(b, gameNode)
        self.branches += [b]

    def newBranches(self, branches = []):
        for b in branches:
            assert isinstance(b, gameNode)
        self.branches += branches

    def is_leaf(self):
        return not self.branches

#Simple Solver

def simple_solver(init, prim, gen, do):
    #generate tree with iterative loop
    #go back up tree, adding W/L: W if L for one of its branches; else, L.
    #return W/L value of root
    root = gameTree(init())
    pos = root.position()
    root.newBranches([gameTree(do(pos, move)) for move in gen(pos)])

    current = root
    for b in root.branches():
        pos = b.position()
        b.newBranches([gameTree(do(pos, move)) for move in gen(pos)])

    return root.status
