def make_grid(x,y):
    """
    :param x: integer - number of columns
    :param y: integer - number of rows
    :return: a dictionary of coordinates representing a grid of x columns and y rows, all with values 0
    """

    return {(i,j):" " for i in range(x) for j in range(y)}




def update_grid(grid, played_position, player):
    """
    :param grid: a dict of coords representing a tic tac toe board
    :param played_position: a tuple of 2 integers representing an available position on the grid
    :param player: "C" for the computer, "U" for the interacting player
    :return: the updated grid with a "O" on the position for the computer and a "X" for the player
    """

    if player == "C":
        grid[played_position] = "X"
    else:
        grid[played_position] = "O"

    return grid




def is_position_valid(grid, position):
    """
    :param grid: a dict of coords representing a tic tac toe board
    :param position: a tuple of two integers
    :return: True if the position is valid and available
    """
    if position not in grid:
        return False
    if grid[position] != " ":
        return False
    else:
        return True
