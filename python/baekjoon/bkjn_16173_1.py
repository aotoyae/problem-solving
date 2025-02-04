import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def dfs(x, y):
    visited[x][y] = 1

    dx = [lst[x][y], 0]
    dy = [0, lst[x][y]]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            dfs(nx, ny)

dfs(0, 0)

print("HaruHaru" if visited[N - 1][N - 1] else "Hing")
