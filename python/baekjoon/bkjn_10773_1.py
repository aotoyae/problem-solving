import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

K = int(input())
lst = []

for _ in range(K):
    n = int(input())

    if n == 0:
        lst.pop()
    else:
        lst.append(n)

print(sum(lst))