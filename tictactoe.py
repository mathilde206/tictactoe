def make_grid(x,y):
    """
    :param x: integer - number of columns
    :param y: integer - number of rows
    :return: a dictionary of coordinates representing a grid of x columns and y rows, all with values 0
    """

    return {(i,j):"0" for i in range(x) for j in range(y)}




