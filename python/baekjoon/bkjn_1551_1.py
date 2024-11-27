import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split(',')))
copy = lst

for _ in range(K):
    for i in range(len(copy) - 1):
        copy[i] = lst[i + 1] - lst[i]
    copy.pop()

print(','.join(map(str, copy)))