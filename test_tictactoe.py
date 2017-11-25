import unittest
from tictactoe import make_grid, update_grid, is_position_valid

class TestTictactoe(unittest.TestCase):

    def test_can_create_an_empty_grid(self):
        self.assertEquals(len(make_grid(2,2)),4)
        self.assertEquals(len(make_grid(3,3)), 9)


    def test_all_coordinates_on_board(self):
        self.assertTrue((0,0) in make_grid(2,2))
        self.assertTrue((1, 0) in make_grid(2, 2))
        self.assertTrue((0, 1) in make_grid(2, 2))
        self.assertTrue((1, 1) in make_grid(2, 2))


    def test_board_starts_empty(self):
        grid = make_grid(2,2)
        self.assertEquals(grid[(0,0)], " ")
        self.assertEquals(grid[(1,0)], " ")
        self.assertEquals(grid[(0,1)], " ")
        self.assertEquals(grid[(1,1)], " ")


    def test_grid_gets_updated(self):
        grid = make_grid(2,2)
        update_grid(grid, (0,0), "U")
        update_grid(grid, (1, 0), "C")
        self.assertEquals(grid[(0,0)], "O")
        self.assertEquals(grid[(1, 0)], "X")
        self.assertEquals(grid[(1, 1)], " ")
        self.assertEquals(grid[(0, 1)], " ")


    def test_position_is_valid(self):
        grid = make_grid(2, 2)
        update_grid(grid, (0, 0), "U")

        self.assertFalse(is_position_valid(grid, (2, 3)))
        self.assertFalse(is_position_valid(grid, (0,0)))
        self.assertTrue(is_position_valid(grid, (1,1)))


    