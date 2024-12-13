import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
total = 0
cnt = 0

while total <= N:
    cnt += 1
    total += cnt

print(cnt - 1)