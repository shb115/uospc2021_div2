import sys

N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

cnt1_1, cnt1_2 = 0, 0
cnt2_1, cnt2_2 = 0, 0
dp = [0] * N
ans1, ans2 = N, 0

if s[0] == '(':
    ans1 = ans1 - 1
    cnt1_1 = cnt1_1 + 1
    cnt2_1 = cnt2_1 + 1
else:
    ans2 = ans2 + 1
    cnt1_1 = cnt1_1 + 1
    cnt2_1 = cnt2_1 + 1

for i in range(1, N - 1):
    if s[i] == '(':
        cnt1_1 = cnt1_1 + 1
        cnt2_1 = cnt2_1 + 1
    else:
        cnt1_2 = cnt1_2 + 1
        cnt2_2 = cnt2_2 + 1

    if cnt2_1 < cnt2_2:
        ans2 = ans2 + 1
        cnt2_1 = cnt2_1 + 1
        cnt2_2 = cnt2_2 - 1

if s[-1] == ')':
    ans1 = ans1 - 1
    cnt1_2 = cnt1_2 + 1
    cnt2_2 = cnt2_2 + 1
else:
    ans2 = ans2 + 1
    cnt1_2 = cnt1_2 + 1
    cnt2_2 = cnt2_2 + 1

ans2 = ans2 + (abs(cnt2_1 - cnt2_2) // 2)

print(ans1)
print(ans2)
