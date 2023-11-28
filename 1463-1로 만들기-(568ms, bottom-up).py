MAX_N = 10**6
INF = 2*MAX_N

# 미리 문제의 답을 구해둔다.
memoize = [INF] * (MAX_N+1)
memoize[1] = 0
for x in range(2, MAX_N+1):
    memoize[x] = 1 + memoize[x-1]
    if x % 3 == 0:
        memoize[x] = min(memoize[x], 1 + memoize[x//3])
    if x % 2 == 0:
        memoize[x] = min(memoize[x], 1 + memoize[x//2])

if __name__ == '__main__':
    print(memoize[int(input())])
