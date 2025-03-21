import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = lst[0]
    
    for i in range(1, N):
        dp[i] = max(dp[i - 1] + lst[i], lst[i])

    print(max(dp))