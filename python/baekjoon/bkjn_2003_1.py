import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
l, r = 0, 1
cnt = 0

while r <= N and l <= r:
    sum_lst = lst[l:r]
    total = sum(sum_lst)

    if total == M:
        cnt += 1
        r += 1
    elif total < M:
        r += 1
    else:
        l += 1

print(cnt)