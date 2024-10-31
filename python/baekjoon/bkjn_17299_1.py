import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
lst = [-1] * N
stack = []
F = dict()

for i in A:
    if i in F: F[i] += 1
    else: F[i] = 1

for i in range(N):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        lst[stack.pop()] = A[i]
    stack.append(i)

print(*lst)