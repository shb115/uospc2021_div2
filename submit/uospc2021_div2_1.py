import sys

N = int(sys.stdin.readline())
s = [int(sys.stdin.readline()) for _ in range(N)]

d = 0
cnt = 0
for i in range(N):
    if s[i] != -1:
        cnt = cnt + 1
        if cnt == 1:
            a = [s[i], i]
        else:
            b = [s[i], i]
            break

d = (b[0] - a[0]) // (b[1] - a[1])

j = 0
for i in range(a[1], -1, -1):
    s[i] = a[0] - d * j
    j = j + 1

for i in range(1, N):
    s[i] = s[i - 1] + d

for i in s:
    print(i)
