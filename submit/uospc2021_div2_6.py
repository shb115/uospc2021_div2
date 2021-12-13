import sys

T, M, N = map(int, sys.stdin.readline().split())

s1, s2 = {}, {}

for _ in range(M):
    s = list(map(int, sys.stdin.readline().split()))
    s1[s] = s[1:]

for _ in range(N):
    s = list(map(int, sys.stdin.readline().split()))
    s2[s] = s[1:]
