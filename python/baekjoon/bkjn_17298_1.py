import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
lst = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        lst[stack.pop()] = A[i]
    stack.append(i)

print(*lst)
