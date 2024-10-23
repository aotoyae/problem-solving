import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
dq = deque()

for _ in range(N):
    cmds = input().split()
    cmd = cmds[0]

    if cmd == "push_front":
        dq.appendleft(cmds[1])
    elif cmd == "push_back":
        dq.append(cmds[1])
    elif cmd == "pop_front":
        print(dq.popleft()) if dq else print(-1)
    elif cmd == "pop_back":
        print(dq.pop()) if dq else print(-1)
    elif cmd == "size":
        print(len(dq))
    elif cmd == "empty":
        print(1) if not dq else print(0)
    elif cmd == "front":
        print(dq[0]) if dq else print(-1)
    elif cmd == "back":
        print(dq[-1]) if dq else print(-1)
