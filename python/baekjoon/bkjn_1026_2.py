import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
A.sort()

for i in range(N):
    B_max = max(B)
    answer += A[i] * B_max
    B.remove(B_max)

print(answer)
