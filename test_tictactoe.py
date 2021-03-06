import unittest
from tictactoe import make_grid, update_grid, get_valid_positions, check_winner

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
        update_grid(grid, (0,0), "Player 1")
        update_grid(grid, (1, 0), "Computer")
        self.assertEquals(grid[(0,0)], "X")
        self.assertEquals(grid[(1, 0)], "O")
        self.assertEquals(grid[(1, 1)], " ")
        self.assertEquals(grid[(0, 1)], " ")

    def test_get_valid_positions(self):
        grid = make_grid(3, 3)
        update_grid(grid, (0, 0), "Player 1")
        self.assertEquals(len(get_valid_positions(grid)), 8)

    def test_finds_winner_diagonal(self):
        grid = make_grid(3,3)
        update_grid(grid, (0, 0), "Player 1")
        self.assertFalse(check_winner(grid))
        update_grid(grid, (1, 1), "Player 1")
        self.assertFalse(check_winner(grid))
        update_grid(grid, (2, 2), "Player 1")
        self.assertTrue(check_winner(grid))

    def test_finds_winner_horizontal(self):
        grid = make_grid(3,3)
        update_grid(grid, (0, 0), "Player 1")
        self.assertFalse(check_winner(grid))
        update_grid(grid, (0, 1), "Player 1")
        self.assertFalse(check_winner(grid))
        update_grid(grid, (0, 2), "Player 1")
        self.assertTrue(check_winner(grid))

    def test_finds_winner_vertical(self):
        grid = make_grid(3,3)
        update_grid(grid, (0, 0), "Player 1")
        self.assertFalse(check_winner(grid))
        update_grid(grid, (1, 0), "Player 1")
        self.assertFalse(check_winner(grid))
        update_grid(grid, (2, 0), "Player 1")
        self.assertTrue(check_winner(grid))