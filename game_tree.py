
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

    def getPosition(self):
        return self.position

    def getParent(self):
        return self.parent

    def getBranches(self):
        return self.branches

    def getStatus(self):
        return self.status

    def newStatus(self, s):
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
