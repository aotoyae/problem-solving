import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int, input().split()))[::-1]
dq = deque()

for i in range(N):
    if A[i] == 1:
        dq.appendleft(i + 1)
    elif A[i] == 2:
        dq.insert(1, i + 1)
    else:
        dq.append(i + 1)

print(*dq)