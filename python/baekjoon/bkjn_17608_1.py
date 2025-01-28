import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
stack = [int(input()) for _ in range(N)]
last = stack[-1]
cnt = 1

for i in reversed(range(N - 1)):
    if stack[i] > last:
        cnt += 1
        last = stack[i]

print(cnt)