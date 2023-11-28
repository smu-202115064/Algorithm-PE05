N = int(input())

memoize = [None] * (N+1)
memoize[0] = 1
memoize[1] = 1

for i in range(1, N+1):
    if i-1 >= 0:
        memoize[i] += memoize[i-1]
    if i-2 >= 0:
        memoize[i] += memoize[i-2]
    memoize[i] %= 10007

print(memoize[N])
