N = int(input())
p, pp = 1, 0
for i in range(1, N+1):
    p, pp = (p + pp) % 10007, p
print(p)
