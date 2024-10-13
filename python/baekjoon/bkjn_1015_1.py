import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A)
P = []

for i in range(N):
    P.append(sorted_A.index(A[i]))
    sorted_A[sorted_A.index(A[i])] = -1

print(*P)
