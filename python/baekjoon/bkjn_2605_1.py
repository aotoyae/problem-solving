import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
answer = []

for i in range(n):
    if lst[i] == 0:
        answer.insert(0, i + 1)
    else:
        answer.insert(lst[i], i + 1)

for i in reversed(answer):
    print(i, end=' ')