import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())

print(int(N * (N - 1) * (N - 2) * (N - 3) / 24))
