import sys

V, E, T = map(int, sys.stdin.readline().split())

link = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v = map(int, sys.stdin.readline().split())
    link[u].append(v)
    link[v].append(u)

dp = [0] * (V + 1)
dp[1] = 1

for i in range(T):
    nxt = [0] * (V + 1)
    for j in range(1, V + 1):
        if dp[j] != 0:
            for k in link[j]:
                nxt[k] = nxt[k] + dp[j]
    dp = nxt

print(sum(dp) % (10 ** 9 + 7))
