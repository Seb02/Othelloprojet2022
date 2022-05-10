import ia
import unittest


def test_basics():
    assert ia.coord(8) == (1,0)
    assert ia.add((2,4),(4,6)) == (6,10)
