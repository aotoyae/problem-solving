import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
answer = []

for i in range(N):
    if 1 in lst[i]:
        for j in range(M):
            if lst[i][j] == 1:
                answer.append((i, j))

print(abs(answer[1][0] - answer[0][0]) + abs(answer[1][1] - answer[0][1]))