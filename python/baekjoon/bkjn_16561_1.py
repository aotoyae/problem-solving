import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input()) // 3

print((n - 1) * (n - 2) // 2)