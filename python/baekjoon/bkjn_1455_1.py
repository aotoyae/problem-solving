import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
coin = [list(map(int, input().strip())) for _ in range(N)]
cnt = 0

def flip(x, y):
    for i in range(x + 1):
        for j in range(y + 1):
            if coin[i][j] == 1:
                coin[i][j] = 0
            else:
                coin[i][j] = 1

for i in range(N - 1, - 1, -1):
    for j in range(M - 1, - 1, -1):
        if coin[i][j]:
            cnt += 1
            flip(i, j)

print(cnt)
