import unittest
from tictactoe import make_grid

class TestTicTacToe(unittest.TestCase):
    def test_can_create_an_empty_grid(self):
        self.assertEquals(len(make_grid(2,2)),4)
        self.assertEquals(len(make_grid(3,3)), 9)

    def test_all_coordinates_on_board(self):
        self.assertIn((0,0) in make_grid(2,2))
        self.assertIn((1, 0) in make_grid(2, 2))
        self.assertIn((0, 1) in make_grid(2, 2))
        self.assertIn((1, 1) in make_grid(2, 2))

    def test_board_starts_empty(self):
        grid = make_grid(2,2)
        self.assertEquals(grid["(0,0)"] == "0")
        self.assertEquals(grid["(1,0)"] == "0")
        self.assertEquals(grid["(0,1)"] == "0")
        self.assertEquals(grid["(1,1)"] == "0")
    