import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(map(int, input().split()))
box = []

def btk(n):
    if n == M:
        print(*box)
        return

    for i in range(N):
        box.append(lst[i])
        btk(n + 1)
        box.pop()

btk(0)