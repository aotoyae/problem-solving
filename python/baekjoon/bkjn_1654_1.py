import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]
start, end = 1, max(lst)

while start <= end:
    mid = (start + end) // 2
    lines = 0

    for i in lst:
        lines += i // mid

    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)