import sys

N = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))

cd = []
j = 0
cnt = 0
cn = c.count(1)
for i in range(N):
    if c[i] == 1:
        j = i
        cnt = 0
        break

for i in range(j + 1, N):
    if c[i] == 1:
        if cnt != 0:
            cd.append(cnt)
            cnt = 0
    else:
        cnt = cnt + 1

for i in range(N):
    if c[i] == 1:
        if cnt != 0:
            cd.append(cnt)
        break
    else:
        cnt = cnt + 1

if cd:
    m = max(cd)
else:
    m = 0

print(max(0, cn - (sum(cd) - m)))
