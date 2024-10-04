import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
answer = 0

for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

for coin in coins:
    if K >= coin:
        answer += K // coin
        K %= coin

        if K <= 0:
            break

print(answer)