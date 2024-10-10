import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
sum = [0]
num = 0

for i in lst:
    num += i
    sum.append(num)

for _ in range(M):
    start, end = map(int, input().split())

    print(sum[end] - sum[start - 1])