import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

A, B, N = map(int, input().split())

for i in range(N):
    A = (A % B) * 10
    result = A // B

print(result)