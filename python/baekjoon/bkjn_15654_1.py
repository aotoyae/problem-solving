import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
box = []

lst.sort()

def btk(n):
    if n == M:
        print(' '.join(map(str, box)))
        return

    for i in range(N):
        if lst[i] in box:
            continue
        box.append(lst[i])
        btk(n + 1)
        box.pop()

btk(0)