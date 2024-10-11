import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

X = int(input())
lst = [64, 32, 16, 8, 4, 2, 1]
cnt = 0

for i in range(len(lst)):
    if X >= lst[i]:
        cnt += 1
        X -= lst[i]
    elif X == 0: break

print(cnt)