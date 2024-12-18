import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    d, t = map(int, input().split())
    lst.append([d, t])

lst.sort(key=lambda lst:lst[1], reverse=True)
time = lst[0][1]

for i in range(n):
    start = lst[i][0]
    end = lst[i][1]

    if time >= end:
        time = end - start
    else:
        time -= start

print(time)
