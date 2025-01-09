from collections import deque

import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
dq = deque([i for i in range(1, N + 1)])
cnt = 0

for num in lst:
    while 1:
        if dq[0] == num:
            dq.popleft()
            break
        else:
            if dq.index(num) <= len(dq) // 2:
                dq.rotate(-1)
                cnt += 1
            else:
                dq.rotate(1)
                cnt += 1

print(cnt)