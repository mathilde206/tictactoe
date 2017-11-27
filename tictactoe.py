import random


def make_grid(x, y):
    """
    :param x: integer - number of columns - in this game, will always be 3
    :param y: integer - number of rows - in this game, will always be 3
    :return: a dictionary of coordinates representing a grid of x columns and y rows, all empty
    """

    return {(i, j): " " for i in range(x) for j in range(y)}


def print_grid(grid):
    """
    :param grid:
    :return:
    """

    for i in range(3):
        string = "| "
        for j in range(3):
            string += str(grid[(i, j)]) + "	|"
        print string


def check_lines(grid):
    """
    :param grid:
    :return: True if there is a full line
    """
    result = False

    #     If there is a not empty, check if can make a line

    #     Make a line:
    #         - all of the same row
    #         - all of the same column
    #         - diagonal

    # # Check horizontal
    #     for i in range(3):
    #         if grid[(i,0)] != 0 and grid[(i,0)] == grid[(i, 1)] and grid[(i, 1)] == grid[(i,2)]:
    #             return True
    #             break
    #
    # # Check vertical
    #     for j in range(3):
    #         if grid[(0, j)] != 0 and grid[(0, j)] == grid[(1, j)] and grid[(1, j)] == grid[(2, j)]:
    #             return True
    #             break
    #
    # # Check diagonal
    #     if grid[(0, 0)] != 0 and grid[(1, )] == grid[(1, j)] and grid[(1, j)] == grid[(2, j)]:
    #         return True
    #         break


    return all_lines


def update_grid(grid, played_position, player):
    """
    :param grid: a dict of coords representing a tic tac toe board
    :param played_position: a tuple of 2 integers representing an available position on the grid
    :param player: "Player 1" for the player 1, "Player 2" for the 2nd player
    :return: the updated grid with a "O" on the position for the computer and a "X" for the player
    """

    if player == "Player 1":
        grid[played_position] = "X"
    else:
        grid[played_position] = "O"

    return grid


def get_valid_positions(grid):
    """
    :param grid: a dict of coords representing a tic tac toe board
    :return: a dict of available positions
    """
    valid_positions = []
    for x in grid:
        if grid[x] == " ":
            valid_positions.append(x)
    return valid_positions

def play(player):
    while True:
        print "%s, it's your turn"%player
        c = int(raw_input("%s, what column do you play?" % player))
        r = int(raw_input("%s, what column do you play?"%player))
        if c in range(3) and r in range(3) and (c, r) in get_valid_positions(grid):
            update_grid(grid, (c, r), player)
            print "%s has played, here is the new board:"%player
            print_grid(grid)
            break;


if __name__ == '__main__':
    grid = make_grid(3,3)
    print "Welcome to Tic Tac Toe"
    print "Player 1, your symbol is X. Player 2, you are O"

    while True:
        play("Player 1")
        break
