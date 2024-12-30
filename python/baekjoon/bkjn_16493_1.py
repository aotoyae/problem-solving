import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(M)]
dp = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(1, M + 1):
    days, pages = lst[i - 1]

    for j in range(1, N + 1):
        if j < days:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - days] + pages)

print(dp[M][N])