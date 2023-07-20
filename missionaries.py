from typing import List, Optional
from generic_search import bfs, Node, node_to_path

MAX_NUM: int = 3

class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.wm: int = missionaries # WEST BANK MISSIONARIES
        self.em: int = MAX_NUM - self.wm # EAST BANK MISSIONARIES
        self.wc: int = cannibals # WEST BANK CANNIBALS
        self.ec: int = MAX_NUM - self.wc # EAST BANK CANNIBALS
        self.boat: bool = boat
        
    def __str__(self) -> str:
        return ("On the west bank there are {} missionaries and {} cannibals.\n"+
                "On the east bank there are {} missionaries and {} cannibals.\n"+
                "the boat is on the {} bank")\
                    .format(self.wm, self.wc, self.em, self.ec, 
                            ("west" if self.boat else "east"))
    
    @property
    def is_legal(self) -> bool:
        if self.wm < self.wc and self.wm > 0:
            return False
        if self.em < self.ec and self.em > 0:
            return False
        return True
    
    def succussors(self) -> List:
        succ: List[MCState] = []
        if self.boat: # boat on west bank
            if self.wm > 1:
                succ.append(MCState(self.wm - 2, self.wc, not self.boat))
            if self.wm > 0:
                succ.append(MCState(self.wm - 1, self.wc, not self.boat))
            if self.wc > 1:
                succ.append(MCState(self.wm, self.wc - 2, not self.boat))
            if self.wc > 0:
                succ.append(MCState(self.wm, self.wc - 1, not self.boat))
            if self.wc > 0 and self.wm > 0:
                succ.append(MCState(self.wm - 1, self.wc - 1, not self.boat))
        else:
            if self.em > 1:
                succ.append(MCState(self.wm + 2, self.wc, not self.boat))
            if self.em > 0:
                succ.append(MCState(self.wm + 1, self.wc, not self.boat))
            if self.ec > 1:
                succ.append(MCState(self.wm, self.wc + 2, not self.boat))
            if self.ec > 0:
                succ.append(MCState(self.wm, self.wc + 1, not self.boat))
            if self.ec > 0 and self.em > 0:
                succ.append(MCState(self.wm + 1, self.wc + 1, not self.boat))
        return [x for x in succ if x.is_legal]
    
    def goal_test(self) -> bool:
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM

def display_solution(path: List[MCState]):
    if len(path) == 0:
        return
    old_state = path[0]
    print(old_state)
    for current_state in path[1:]:
        if current_state.boat:
            print("{} missionaries and {} cannibals moved from the east bank to the west bank.\n"
                .format(old_state.em - current_state.em, old_state.ec -current_state.ec))
        else:
            print("{} missionaries and {} cannibals moved from the west bank to the east bank.\n"
                  .format(old_state.wm - current_state.wm, old_state.wc -current_state.wc))
        print(current_state)
        old_state = current_state
    

# SOLVing:

start: MCState = MCState(MAX_NUM, MAX_NUM, True)
solution: Optional[Node[MCState]] = bfs(start, MCState.goal_test, MCState.succussors)
if solution is None:
    print("No solution Found")
else:
    path: List[MCState] = node_to_path(solution)
    display_solution(path)
                  