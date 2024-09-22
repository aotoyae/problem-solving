import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n, m = map(int, input().split())
board = []
lst = []

for _ in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        x = 0
        y = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] == 'W': x += 1
                    else: y += 1
                else:
                    if board[a][b] == 'B':
                        x += 1
                    else:
                        y += 1

        lst.append(x)
        lst.append(y)

print(min(lst))