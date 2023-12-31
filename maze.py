from enum import Enum
from typing import NamedTuple, List, Optional, Callable
import random
from generic_search import dfs, Node, node_to_path, bfs, astar
import math

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
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.col] != Cell.BLOCKED: # UP
            locations.append(MazeLocation(ml.row+1, ml.col))
        if ml.row - 1 > -1 and self._grid[ml.row - 1][ml.col] != Cell.BLOCKED: # DOWN
            locations.append(MazeLocation(ml.row-1, ml.col))
        if ml.col + 1 < self._cols and self._grid[ml.row][ml.col + 1] != Cell.BLOCKED: # RIGHT
            locations.append(MazeLocation(ml.row, ml.col + 1))
        if ml.col - 1 > -1 and self._grid[ml.row][ml.col - 1] != Cell.BLOCKED: # LEFT
            locations.append(MazeLocation(ml.row, ml.col - 1))
        return locations
    
    def mark(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.col] = Cell.PATH
        self._grid[self.start.row][self.start.col] = Cell.START
        self._grid[self.goal.row][self.goal.col] = Cell.GOAL
    
    def clear(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.col] = Cell.EMPTY
        self._grid[self.start.row][self.start.col] = Cell.START
        self._grid[self.goal.row][self.goal.col] = Cell.GOAL
    
    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + '\n'
        return output



def euclidean_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        xdist: int = ml.col - goal.col
        ydist: int = ml.row - goal.row
        return math.sqrt(xdist**2+ydist**2)
    return distance

def manhattan_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        xdist: int = abs(ml.col - goal.col)
        ydist: int = abs(ml.row - goal.row)
        return (xdist+ydist)
    return distance

# TEST

maze: Maze = Maze()
print(maze)

# TEST DFS
solution1: Optional[Node[MazeLocation]] = dfs(maze.start, maze.goal_test, maze.successors)
if solution1 is None:
    print("No solution Found")
else:
    path1: List[MazeLocation] = node_to_path(solution1)
    maze.mark(path1)
    print(maze)
    maze.clear(path1)
    
# TEST BFS
solution2: Optional[Node[MazeLocation]] = bfs(maze.start, maze.goal_test, maze.successors)
if solution2 is None:
    print("No solution Found.")
else:
    path2: List[MazeLocation] = node_to_path(solution2)
    maze.mark(path2)
    print(maze)
    maze.clear(path1)
    
# TEST A*
distance: Callable[[MazeLocation], float] = manhattan_distance(maze.goal)
solution3: Optional[Node[MazeLocation]] = astar(maze.start, maze.goal_test, maze.successors, distance)
if solution3 is None:
    print("No solution Found.")
else:
    path3: List[MazeLocation] = node_to_path(solution3)
    maze.mark(path3)
    print(maze)
    maze.clear(path3)