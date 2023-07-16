from enum import Enum
from typing import NamedTuple, List
import random

class Cell(str, Enum):
    EMPTY = "E"
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazeLocation(NamedTuple):
    row: int
    col: int

class Maze:
    def __init__(self, rows: int = 10, cols: int = 10, 
                 spareness: float = 0.2, 
                 start:MazeLocation = MazeLocation(0,0),
                 goal: MazeLocation = MazeLocation(9,9)) -> None:
        self._rows = rows
        self._cols = cols
        self.start = start
        self.goal = goal
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(cols)] for r in range(rows)]
        self._randomly_fill(rows, cols, spareness)
        self._grid[start.row][start.col] = Cell.START
        self._grid[goal.row][goal.col] = Cell.GOAL
        
    def _randomly_fill(self, rows:int, cols:int, spareness:float):
        for row in range(rows):
            for col in range(cols):
                if random.uniform(0, 1.0) < spareness:
                    self._grid[row][col] = Cell.BLOCKED
    
    def goal_test(self, ml: MazeLocation):
        if ml == self.goal:
            return True
        return False
    
    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.col] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row+1, ml.col))
        if ml.row - 1 > -1 and self._grid[ml.row - 1][ml.col] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row-1, ml.col))
        if ml.col + 1 < self._cols and self._grid[ml.row][ml.col + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.col + 1))
        if ml.col - 1 > -1 and self._grid[ml.row][ml.col - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.col - 1))
        return locations
    
    
    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + '\n'
        return output

maze: Maze = Maze()
print(maze)