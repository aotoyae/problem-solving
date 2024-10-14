import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0

A.sort(reverse=True)
B.sort()

for i in range(len(A)):
    cnt += A[i] * B[i]

print(cnt)