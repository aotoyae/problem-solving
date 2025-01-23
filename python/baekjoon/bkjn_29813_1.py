import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque([list(input().split()) for _ in range(N)])

while len(queue) > 1:
    name, num = queue.popleft()

    for _ in range(int(num) - 1):
        queue.append(queue.popleft())
    queue.popleft()

print(queue[0][0])