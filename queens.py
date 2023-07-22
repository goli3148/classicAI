from typing import Dict, List, Optional
from csp import Constraint, CSP

class QueensConstraint(Constraint[int, int]):
    def __init__(self, coloumns: List[int]) -> None:
        super().__init__(coloumns)
        self.coloumns: List[int] = coloumns
    
    def satisfied(self, assignment: Dict[int, int]) -> bool:
        for q1c, q1r in assignment.items():
            for q2c, q2r in assignment.items():
                if q2c == q1c and q2r == q1r : continue
                if q2c == q1c or q2r == q1r:
                    return False
                if abs(q2c - q1c) == abs(q2r - q1r):
                    return False
        return True

if __name__ == "__main__":
    columns: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    rows: Dict[int, List[int]] = {}
    for column in columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
    csp: CSP[int, int] = CSP(columns, rows)
    csp.add_constraint(QueensConstraint(columns))
    solution: Optional[Dict[int, int]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)