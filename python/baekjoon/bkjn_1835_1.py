import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
from collections import deque

N = int(input())
dq = deque()
dq.append(N)

for i in range(N - 1, 0, -1):
    dq.appendleft(i)

    for j in range(i):
        dq.appendleft(dq.pop())

print(*dq)