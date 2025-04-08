import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

colors = set()

for _ in range(2):
    parents = input().split()

    for p in parents:
        colors.add(p)

lst = sorted(list(colors))

for i in lst:
    for j in lst:
        print(i, j)