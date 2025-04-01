import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
point = []

for _ in range(N):
    lst = list(map(int, input().split()))
    run = lst[:2]
    trick = sorted(lst[2:])
    point.append(max(run) + trick[3] + trick[4])

print(max(point))