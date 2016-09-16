import nose
from simple_solver import simple_solver

def initial_position():
    return 4

def primitive(pos):
    if pos <= 0:
        return True
    return False

def gen_moves(pos):
    if pos == 0:
        return []
    if pos == 1:
        return [-1]
    return [-2, -1]

def do_moves(pos, move):
    assert pos + move >= 0
    return pos + move

def test():
    result = simple_solver(initial_position, primitive, gen_moves, do_moves)
    assert result == "Draw"

nose.main()
