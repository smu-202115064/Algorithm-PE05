import sys

MAX_N = 1000
sys.setrecursionlimit(2*MAX_N)

N = int(input())

memoize = [None] * (N+1)
memoize[0] = 1
memoize[1] = 1

def solve(n: int) -> int:
    if memoize[n] is None:
        memoize[n] = (solve(n-1) + solve(n-2)) % 10007
    return memoize[n]

print(solve(N))
