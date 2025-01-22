import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
queue = []
max = [0, 0]

for _ in range(n):
    lst = list(map(int, input().split()))

    if len(lst) == 1:
        queue.pop(0)
    else:
        queue.append(lst[1])

    if max[0] < len(queue):
        max[0] = len(queue)
        max[1] = queue[-1]
    elif max[0] == len(queue):
        max[1] = min(max[1], queue[-1])

print(*max)