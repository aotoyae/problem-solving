import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()

answer = []

for i in range(N):
    cnt = 0

    for j in range(lst[i], lst[i] + 5):
        if j not in lst:
            cnt += 1

    answer.append(cnt)

print(min(answer))