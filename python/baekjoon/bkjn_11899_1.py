import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

S = input().strip()
stack = []
cnt = 0

for i in S:
    if i == '(':
        stack.append('(')
    else:
        if stack:
            stack.pop()
        else:
            cnt += 1

print(len(stack) + cnt)