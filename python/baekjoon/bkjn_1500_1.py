import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

S, K = map(int, input().split())
lst = [S // K for _ in range(K)]

for i in range(S % K):
    lst[i] += 1

num = 1

for i in lst:
    num *= i

print(num)