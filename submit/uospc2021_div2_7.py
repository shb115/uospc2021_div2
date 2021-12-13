import sys

N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
y = list(map(int, sys.stdin.readline().split()))

cnt = []
brokenx = set()
brokeny = set()

for i in range(N):
    for j in range(N):
        t1 = (j + 1) / x[i]
        t2 = (i + 1) / y[j]
        if t1 == t2:
            cnt.append([t1, i, j])

cnt.sort()

for i in cnt:
    if i[1] not in brokenx and i[2] not in brokeny:
        brokenx.add(i[1])
        brokeny.add(i[2])

print(len(brokenx))
