import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = [list(input().strip()) for _ in range(N)]
f = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if j == k:
                continue
            if lst[j][k] == 'Y' or (lst[j][i] == 'Y' and lst[i][k] == 'Y'):
                f[j][k] = 1

res = 0

for row in f:
    res = max(res, sum(row))

print(res)