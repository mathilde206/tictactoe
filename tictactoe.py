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


def check_winner(grid):
    """
    :param grid:  a dict of coords representing a tic tac toe board
    :return: True if there is a full line, False, if there isn't
    """

    # Check horizontal
    for i in range(3):
        if grid[(i,0)] != " " and grid[(i,0)] == grid[(i,1)] and grid[(i,1)] == grid[(i,2)]:
            if grid[(i,0)] == "X":
                print "Player 1, you won"
                return True
            else:
                print "Computer, you won"
                return True

    for j in range(3):
        if grid[(0, j)] != " " and grid[(0, j)] == grid[(1, j)] and grid[(1, j)] == grid[(2 , j)]:
            if grid[(0, j)] == "X":
                print "Player 1, you won"
                return True
            else:
                print "Computer, you won"
                return True

    if grid[(0, 0)] != " " and grid[(0, 0)] == grid[(1, 1)] and grid[(1, 1)] == grid[(2 , 2)]:
        if grid[(0, 0)] == "X":
            print "Player 1, you won"
            return True
        else:
            print "Computer, you won"
            return True

    if grid[(0, 2)] != " " and grid[(0, 2)] == grid[(1, 1)] and grid[(1, 1)] == grid[(2, 0)]:
        if grid[(0, 2)] == "X":
            print "Player 1, you won"
            return True
        else:
            print "Computer, you won"
            return True

    return False

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
        try:
            x = int(raw_input("%s, what row do you play?" % player))
            y = int(raw_input("%s, what column do you play?"%player))
        except:
            print "Please enter an integer"
        else:
            if x in range(3) and y in range(3) and (x, y) in get_valid_positions(grid):
                update_grid(grid, (x, y), player)
                print "%s has played, here is the new board:"%player
                print_grid(grid)
                break
            elif x not in range(3) or y not in range(3):
                print "You must enter an integer between 0 and 2 - 0 is the first column and 2 is the 3rd"
            else:
                print "This is not a valid position"

def computer_play(valid_pos):
    """
    :param valid_pos: gets an array of available positions
    :return:
    """
    i = random.randint(0, len(valid_pos)-1)
    update_grid(grid, valid_pos[i], "Computer")
    print "Computer has played, here is the new board:"
    print_grid(grid)



if __name__ == '__main__':
    grid = make_grid(3,3)
    print "Welcome to Tic Tac Toe"
    print "Player 1, your symbol is X. Player 2, you are O"

    while True:
        play("Player 1")

        if check_winner(grid):
            break

        valid_pos = get_valid_positions(grid)
        computer_play(valid_pos)

        if check_winner(grid):
            break
