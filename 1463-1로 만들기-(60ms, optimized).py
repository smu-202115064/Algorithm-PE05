import sys


def solve(x: int) -> int:
    if memoize[x] is None:
        # 하나 씩 감소하는 케이스는 그냥 나머지 산술 연산으로 대체하면,
        # T(n) = T(n-1) + f(n) 꼴에서, T(n) = aT(n/b) + f(n) 꼴로
        # 부분 문제의 입력데이터의 크기가 줄어드는 점화식으로 표현할 수 있게 된다.
        # 메모이제이션까지 사용하여, 동일한 x에 대한 solve(x)값은 단 1회만 계산하기에,
        # O(log N) 시간 복잡도로 줄일 수 있게 된다.
        memoize[x] = 1 + min(x % 3 + solve(x//3), x % 2 + solve(x//2))
    return memoize[x]


MAX_N = 10**6
sys.setrecursionlimit(2*MAX_N)
memoize = [None] * (MAX_N+1)
memoize[0] = 0
memoize[1] = 0
solve(MAX_N)

if __name__ == '__main__':
    print(solve(int(sys.stdin.readline())))
