import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
lst = []

def dfs(start):
    if len(lst) == M:
        print(*lst)
        return

    for i in range(start, N):
        lst.append(nums[i])
        dfs(i)
        lst.pop()

dfs(0)