from enum import Enum
from typing import List, NamedTuple

import random

class Cell(str, Enum):
    EMPTY = ".",
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "#"

class MazeLocation(NamedTuple):
    row: int
    column: int

class Maze:
    def __init__(self,
                 rows: int,
                 columns : int,
                 sparsness : float,
                 start : MazeLocation,
                 goal : MazeLocation):

        self._rows = rows # Size Baris Maze
        self._columns = columns # Size Kolom Maze

        self.start: MazeLocation = start
        self.goal: MazeLocation = goal

        # a = MazeLocation(2, 3)
        
        # koordinat_start = [2, 3]
        # x_start = koordinat_start[0]
        # y_start = koordinat_start[1]

        # koordinat_start = MazeLocation(2, 3)
        # x_start = koordinat_start.x
        # y_start = koordinat_start.y

        # # cara list
        # cell = [".", "X", "S", "G", "#"]
        # blocked = cell[1]

        # Cara Class Enum
        # cell = Cell()
        # cell.BLOCKED
        
        # Mebuat labirin / maze kosong tanpa tembok / block
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        
        # Membuat labirin tembok
        self._random_block(rows, columns, sparsness)

        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL
                


    def _random_block(self, rows: int, columns: int, sparsness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) > sparsness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self):
        output = ''
        for row in self._grid:
            output += "|".join([c for c in row]) + '\n'
        return output

    def goal_test(self, ml: MazeLocation) -> bool:
        # Cek apakah pathfinder sudah menemukan goal
        return ml == self.goal

    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        # cek area sekitar apakah bisa di lewati atau tidak
        locations: List[MazeLocation] = []
        #ml.row = koordinat saat ini self._rows = size maze
        if ml.row > self._rows or ml.column > self._columns or ml.row < 0 or ml.column <0:
            raise ValueError(f'{ml} merupakan lokasi yang salah dengan maze yang berukuran {self._rows, self._columns}')
        
        # cek apakah bisa ke bawah
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))

        # cek apakah bisa ke atas
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))

        # cek apakah bisa ke kanan
        if ml.column - 1 < self._columns and self._grid[ml.row, ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))

        # cek apakah bisa ke kiri
        if ml.column - 1 >= 0 and self._grid[ml.row, ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))

        return locations
