from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar("V") # variable
D = TypeVar("D") # domain

class Constraint(Generic[V, D], ABC):
    def __init__(self, varaibles: List[V]) -> None:
        self.variables = varaibles
    
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...
        
class CSP(Generic[V, D]):
    def __init__(self, varaibles: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = varaibles
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for varaible in self.variables:
            self.constraints[varaible] = []
            if varaible not in self.domains:
                raise LookupError("Every Variable should have a domain assing to it.")
    
    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint is not in CSP.")
            else:
                self.constraints[variable].append(constraint)
    
    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True
    
    def backtracking_search(self, assignment: Dict[V, D]={}) -> Optional[Dict[V, D]]:
        if len(assignment) == len(self.variables): return assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        local_assignment = assignment.copy()
        varaible = unassigned[0]
        for domain in self.domains[varaible]:
            local_assignment[varaible] = domain
            if self.consistent(varaible, local_assignment):
                result = self.backtracking_search(local_assignment)
                if not result == None:
                    return result
        return None
         
