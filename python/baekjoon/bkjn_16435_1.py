import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, L = map(int, input().split())
lst = sorted(list(map(int, input().split())))

for fruit in lst:
    if fruit <= L:
        L += 1
    else:
        break

print(L)