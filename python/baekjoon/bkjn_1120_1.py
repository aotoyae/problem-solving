import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

A, B = input().split()
lst = []

for i in range(len(B) - len(A) + 1):
    cnt = 0

    for j in range(len(A)):
        if A[j] != B[i + j]:
            cnt += 1

    lst.append(cnt)

print(min(lst))