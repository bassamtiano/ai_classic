import random
from tools.maze import *

def random_coordinate(size_rows, size_column, start_column = None, start_row = None):
    # Find Start Coordinate Column
    column = random.randint(0, size_column - 1)

    # Find Goal Coordinate Column
    if start_column is not None:
        while column == start_column:
            # Jika hasil random sama dengan koordinat start column akan terus loop
            column = random.randint(0, size_column - 1)

    # Find Start Coordinate Row
    row = random.randint(0, size_rows - 1)

    # Find Goal Coordinate Row
    if start_row is not None:
        while row == start_row:
            row = random.randint(0, size_rows - 1)
        
    return row, column

if __name__ == "__main__":

    size_rows = 15
    size_columns = 10

    # Random Koordinat Start
    start_row, start_column = random_coordinate(size_rows, size_columns)

    # Random Koordinat Goal
    goal_row, goal_column = random_coordinate(size_rows, size_columns, start_row, start_column)

    start = MazeLocation(start_row, start_column)
    goal = MazeLocation(goal_row, goal_column)

    my_maze = Maze(rows = size_rows, columns = size_columns, start = start, goal = goal, sparsness = 0.8)
    print(my_maze)