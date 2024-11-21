import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    nums = list(map(int, input().split()))
    lst.append(nums)

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            lst[i][j] += lst[i - 1][j]
        elif j == i:
            lst[i][j] += lst[i - 1][j - 1]
        else:
            lst[i][j] += max(lst[i - 1][j - 1], lst[i - 1][j])

print(max(lst[-1]))