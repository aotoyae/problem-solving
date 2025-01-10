import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
P = int(input())
lst = set()
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for i in range(P):
    A, B = map(int, input().split())
    graph[A] += [B]
    graph[B] += [A]

def dfs(c):
    visited[c] = 1

    for n in graph[c]:
        if visited[n] == 0:
            dfs(n)

dfs(1)
print(sum(visited) - 1)
