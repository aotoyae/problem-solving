import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
lst = [[0] * 100 for _ in range(100)]
result = 0

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            lst[i][j] = 1

for num in lst:
    result += num.count(1)

print(result)
