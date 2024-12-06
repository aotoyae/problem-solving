import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
dic = { -1: 0, 0: 0, 1: 0 }

def divided(row, col, n):
    curr = paper[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if paper[i][j] != curr:
                next = n // 3
                divided(row, col, next)
                divided(row, col + next, next)
                divided(row, col + next*2, next)
                divided(row + next, col, next)
                divided(row + next, col + next, next)
                divided(row + next, col + next*2, next)
                divided(row + next*2, col, next)
                divided(row + next*2, col + next, next)
                divided(row + next*2, col + next*2, next)
                return

    dic[curr] += 1
    return

divided(0, 0, N)

for i in dic.values():
    print(i)
