import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

A, B = map(int, input().split())
N = int(input())

answer = abs(A - B)

for _ in range(N):
    num = int(input())
    if answer > abs(num - B):
        answer = abs(num - B) + 1

print(answer)