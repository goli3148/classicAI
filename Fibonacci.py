from typing import Dict, Generator
from timeC import  timeC
from functools import lru_cache

# RECURSIVE
def fib(n: int)->int:
    return fib(n-1) + fib(n-2) if n >= 2 else n

# Memoization
memory:Dict[int, int] = {0:0, 1:1}
def fib1(n: int)->int:
    global memory
    if n not in memory:
        memory[n] = fib1(n-1) + fib1(n-2)
    return memory[n]

# Aitomatic Memoization (built-in decorator)
@lru_cache(maxsize=None)
def fib2(n:int)->int:
    if n < 2:
        return n
    return fib2(n-2) + fib2(n-1)

# Iterative Approach
def fib4(n:int)->int:
    if n==0: return 0
    last: int = 0
    next: int = 1
    for _ in range(1,n):
        last, next = next, last+next
    return next


# timeC().Cal(fib, 35)
# timeC().Cal(fib1, 35)
# timeC().Cal(fib2, 35)
# timeC().Cal(fib4, 35)



# Fibonacci Generator
def fib5(n:int)->Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, next+last
        yield next

for i in fib5(50):
    print(i, end=',')
