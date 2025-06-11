import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())

lst = []
cnt = 0

for _ in range(M):
    A, B = map(int, input().split())

    if A < N:
        lst.append([A, B])
    else:
        cnt += 1

lst.sort(reverse=True)
result = 0

if M - 1 == cnt:
    print(0)
else:
    for i in range(M - 1 - cnt):
        result += (N - lst[i][0])
    print(result)