import sys

N = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))

cd = []
j = 0
cnt = 0
for i in range(N):
    if c[i] == 1:
        j = i
        cnt = 0
        break

for i in range(j + 1, N):
    cnt = cnt + 1
    if c[i] == 1:
        cd.append(cnt)
        cnt = 0

for i in range(N):
    cnt = cnt + 1
    if c[i] == 1:
        cd.append(cnt)
        break

if cd:
    print(N - max(cd))
else:
    print(0)
