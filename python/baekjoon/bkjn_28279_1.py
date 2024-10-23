import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
dq = deque()

for _ in range(N):
    cmds = input().split()
    cmd = cmds[0]

    if cmd == "1":
        dq.appendleft(cmds[1])
    elif cmd == "2":
        dq.append(cmds[1])
    elif cmd == "3":
        print(dq.popleft()) if dq else print(-1)
    elif cmd == "4":
        print(dq.pop()) if dq else print(-1)
    elif cmd == "5":
        print(len(dq))
    elif cmd == "6":
        print(1) if not dq else print(0)
    elif cmd == "7":
        print(dq[0]) if dq else print(-1)
    elif cmd == "8":
        print(dq[-1]) if dq else print(-1)
