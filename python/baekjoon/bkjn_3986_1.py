import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(N):
    stack = []
    lst = list(input().strip())

    for i in lst:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)

    if not stack:
        cnt += 1

print(cnt)