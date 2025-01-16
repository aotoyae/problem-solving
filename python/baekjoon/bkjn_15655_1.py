import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
box = []

lst.sort()

def btk(idx):
    if len(box) == M:
        print(*box)
        return

    for i in range(idx, N):
        if lst[i] not in box:
            box.append(lst[i])
            btk(i + 1)
            box.pop()

btk(0)