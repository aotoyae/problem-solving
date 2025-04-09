import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, K = map(int, input().split())
lst = [0] + sorted(map(int, input().split()))
time = []

for i in range(len(lst) - 1, 0, -1):
    time.append(lst[i] - lst[i - 1])

answer = sorted(time, reverse=True)[K:]
print(sum(answer))