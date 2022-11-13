from calculator import MiniCalculator

mc = MiniCalculator(10, 5)
def test1():
    assert mc.add() == 15
def test_substract():
    assert mc.substract() == 5

def test_subtract_reverse():
    assert mc.substract(reverse=True) == -5