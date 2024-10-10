import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
lst = []

def dfs(start):
    if len(lst) == M:
        print(' '.join(map(str, lst)))
        return

    for i in range(start, N + 1):
        lst.append(i)
        dfs(i)
        lst.pop()

dfs(1)
