import sys

N, M = map(int, sys.stdin.readline().split())
lib = [sys.stdin.readline().rstrip() for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if lib[i][j] == 'C':
            if lib[i - 1][j] != 'P' and lib[i + 1][j] != 'P' and lib[i][j - 1] != 'P' and lib[i][j + 1] != 'P':
                cnt = cnt + 1

print(cnt)
