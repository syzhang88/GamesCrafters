import nose
from simple_solver import simple_solver, primitive, do_moves

def initial_position():
    return pos

def gen_moves(pos):
    if pos == 0:
        return []
    if checker(pos):
        return [a]
    return [a, b]

pos = 1
checker = lambda x: pos == 0
a, b = -1, -2

def test_win():
    result = simple_solver(initial_position, primitive, gen_moves, do_moves)
    assert result == "Win"

pos = 4
a, b = -1, -2

def test_lose():
    result = simple_solver(initial_position, primitive, gen_moves, do_moves)
    assert result == "Win"

checker = lambda x: False
a, b = -1, 1

def test_draw():
    result = simple_solver(initial_position, primitive, gen_moves, do_moves)
    assert result == "Draw"

a, b = 1, 2

def test_draw2():
    result = simple_solver(initial_position, primitive, gen_moves, do_moves)
    assert result == "Draw"

nose.main()
