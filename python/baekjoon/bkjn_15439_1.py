import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())

print(N * (N - 1))