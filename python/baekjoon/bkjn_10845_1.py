import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

queue = []
N = int(input())

for _ in range(N):
    cmds = input().split()
    cmd = cmds[0]

    if cmd == 'push':
        queue.append(cmds[1])
    elif cmd == 'pop':
        print(queue.pop(0)) if queue else print(-1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        print(0) if queue else print(1)
    elif cmd == 'front':
        print(queue[0]) if queue else print(-1)
    else:
        print(queue[-1]) if queue else print(-1)
