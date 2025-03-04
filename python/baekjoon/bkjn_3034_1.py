import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, W, H = map(int, input().split())
C = (W ** 2 + H ** 2) ** 0.5

for _ in range(N):
    match = int(input())

    print('DA' if match <= C else 'NE')