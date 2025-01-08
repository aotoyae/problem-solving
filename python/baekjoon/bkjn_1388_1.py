import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
cnt = 0

for i in range(N):
    a = ''

    for j in range(M):
        if graph[i][j] == '-' and graph[i][j] != a:
            cnt += 1
        a = graph[i][j]

for j in range(M):
    a = ''

    for i in range(N):
        if graph[i][j] == "|" and graph[i][j] != a:
            cnt += 1
        a = graph[i][j]

print(cnt)