import functools
import sys


@functools.cache
def solve(k: int, n: int) -> int:
    if k == 0:
        return n
    if n == 1:
        return 1
    return solve(k-1, n) + solve(k, n-1)


if __name__ == '__main__':
    for t in range(int(sys.stdin.readline())):
        k = int(sys.stdin.readline())
        n = int(sys.stdin.readline())
        print(solve(k, n))
