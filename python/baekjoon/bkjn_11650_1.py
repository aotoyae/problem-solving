import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    [x, y] = map(int, input().split())
    arr.append([x, y])

arr.sort()

for i in arr:
    print(i[0], i[1])

n = int(input())
arr = []

for i in range(n):
    [x, y] = map(int, input().split())
    arr.append([x, y])

arr.sort()

for i in arr:
    print(i[0], i[1])