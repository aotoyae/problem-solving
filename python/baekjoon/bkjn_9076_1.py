import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())

for _ in range(N):
    lst = sorted(map(int, input().split()))
    answer = lst[1] + lst[2] + lst[3]

    print(answer if lst[3] - lst[1] < 4 else 'KIN')