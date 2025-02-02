import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = [[' ' for _ in range(4 * N - 3)] for _ in range(4 * N - 3)]

def star(n, x, y):
    if n == 1:
        lst[y][x] = '*'
        return

    l = 4 * n - 3

    for i in range(l):
        lst[y][x + i] = '*'
        lst[y + i][x] = '*'
        lst[y + l - 1][x + i] = '*'
        lst[y + i][x + l - 1] = '*'

    star(n - 1, x + 2, y + 2)

star(N, 0, 0)

for i in lst:
    print(''.join(i))