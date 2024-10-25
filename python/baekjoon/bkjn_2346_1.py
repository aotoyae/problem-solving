import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
queue = deque(enumerate(map(int, input().split())))
lst = []

while queue:
    idx, num = queue.popleft()
    lst.append(idx + 1)

    if num > 0:
        queue.rotate(-(num - 1))
    elif num < 0:
        queue.rotate(-num)

print(*lst)
