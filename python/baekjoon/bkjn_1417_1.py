import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
dasom = int(input())
vote = [int(input()) for _ in range(N - 1)]
cnt = 0

vote.sort(reverse=True)

if N == 1:
    print(0)
else:
    while vote[0] >= dasom:
        dasom += 1
        vote[0] -= 1
        cnt += 1
        vote.sort(reverse=True)

    print(cnt)