"""
test cases to check if square validity check works
"""

from square import Square
from point import Point

def test_straight_square():
    p1 = Point(0, 0)
    p2 = Point(1, 1)
    p3 = Point(1, 0)
    p4 = Point(0, 1)
    square = Square(p1, p2, p3, p4)
    assert square.check_valid_square() == True

def test_invalid_square():
    p1 = Point(0, 0)
    p2 = Point(1, 1)
    p3 = Point(1, 0)
    p4 = Point(0, 12)
    square = Square(p1, p2, p3, p4)
    assert square.check_valid_square() == False

def test_rotated_square():
    p1 = Point(1, 0)
    p2 = Point(-1, 0)
    p3 = Point(0, 1)
    p4 = Point(0, -1)
    square = Square(p1, p2, p3, p4)
    assert square.check_valid_square() == True