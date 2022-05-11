import ia
import unittest

state1 = {'players': ['Random', 'IA_20034_20342'], 'current': 0, 'board': [[26, 22, 21, 44, 35, 4, 13, 38, 36, 37, 19, 27], [42, 28, 20, 45, 46, 17, 18, 2, 10, 11]]}
state2 = {'players': ['IA_20034_20342', 'Random'], 'current': 0, 'board': [[2, 4, 3, 7, 14, 0, 1, 9, 16, 19, 23, 15, 37, 63, 45, 27, 32, 24, 25, 17, 58, 10, 18, 26, 44, 20, 28, 12, 56, 57, 59, 60, 61, 62, 50, 6, 5, 13, 48, 40, 41], [30, 29, 21, 31, 22, 11, 54, 38, 46, 43, 36, 53, 55, 39, 47, 42, 33, 34, 35]]}
state3 = {'players': ['Random', 'IA_20034_20342'], 'current': 0, 'board': [[17, 3, 10],[6, 35, 27, 9, 14, 49, 54, 11, 12, 25, 30, 33, 38, 51, 52, 19, 20, 26, 29, 34, 37, 43, 44, 4, 24, 31, 32, 39, 59, 60, 2, 10, 18, 17, 16, 40, 41, 42, 50, 58, 61, 53, 45, 46, 47, 5, 13, 21, 22, 23, 0, 7, 56, 63]]}
def test_basics():
    assert ia.coord(8) == (1,0)
    assert ia.add((2,4),(4,6)) == (6,10)
def test_Coupchoisi():
    assert ia.Coupchoisi(state1['board'][0]+state1['board'][1], ia.PossibleMoves(state1), state1)== 53
    assert ia.Coupchoisi(state2['board'][0]+state2['board'][1], ia.PossibleMoves(state2), state2)== 49
    assert ia.Coupchoisi(state3['board'][0]+state3['board'][1], ia.PossibleMoves(state3), state3)== 1
