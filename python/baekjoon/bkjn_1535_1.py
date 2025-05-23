import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
L_lst = [0] + list(map(int, input().split()))
J_lst = [0] + list(map(int, input().split()))
dp = [[0] * 101 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 101):
        if L_lst[i] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - L_lst[i]] + J_lst[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][99])