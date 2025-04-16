import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input()) - 1
M = int(input()) - 1

print(N * M * 2)