from typing import Dict, NamedTuple, List, Optional
from random import choice
from string import ascii_uppercase
from csp import Constraint, CSP

Grid = List[List[str]]

class GridLocation(NamedTuple):
    row: int
    col: int
    def __str__(self) -> str:
        return f"({self.row},{self.col})"

def generated_grid(rows: int, cols: int) -> Grid:
    return [["*" for _ in range(cols)] for _ in range(rows)]
    return [[choice(ascii_uppercase) for c in range(cols)] for r in range(rows)]

def display_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))

def generate_domain(word: str, grid: Grid) -> List[List[GridLocation]]:
    col: int = len(grid[0])
    row: int = len(grid)
    word_len: int = len(word)
    domain: List[List[GridLocation]] = [] # [ [ start_location, end_location ] ]
    
    for i in range(row):
        for j in range(col):
            if col - j >= word_len and row - i >= word_len:
                # domain.append([GridLocation(i, j), GridLocation(i + word_len - 1, j + word_len - 1)])
                domain.append([GridLocation(i + count ,j + count) for count in range(0, word_len)])
            if col - j >= word_len:
                # domain.append([GridLocation(i, j), GridLocation(i, j + word_len - 1)])
                domain.append([GridLocation(i ,col_j) for col_j in range(j, j + word_len)])
            if row - i >= word_len:
                # domain.append([GridLocation(i, j), GridLocation(i + word_len - 1, j)])
                domain.append([GridLocation(row_i, j) for row_i in range(i, i + word_len)])
            
    return domain

class WordSearchConstraint(Constraint[str, List[GridLocation]]):
    def __init__(self, words: List[str]) -> None:
        super().__init__(words)
        self.words: List[str] = words
    def satisfied(self, assignment: Dict[str, List[GridLocation]]) -> bool:
        all_loc: List[GridLocation] = [locs for vals in assignment.values() for locs in vals]
        return len(set(all_loc)) == len(all_loc)

if __name__ == "__main__":
    grid: Grid = generated_grid(9, 9)
    words: List[str] = ["MATTHEW","ALI"]
    locations: Dict[str, List[List[GridLocation]]] = {}
    for word in words:
        locations[word] = generate_domain(word, grid)
    
    csp: CSP[str, List[GridLocation]] = CSP(words, locations)
    csp.add_constraint(WordSearchConstraint(words))
    solution: Optional[Dict[str, List[GridLocation]]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        for word, grid_locations in solution.items():
            if choice([True, False]):
                grid_locations.reverse()
            for index, letter in enumerate(word):
                (row, col) = (grid_locations[index].row, grid_locations[index].col)
                grid[row][col] = letter
        display_grid(grid)