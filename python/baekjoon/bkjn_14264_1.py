import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

L = int(input())

print((3 ** 0.5 * L ** 2) / 4)
