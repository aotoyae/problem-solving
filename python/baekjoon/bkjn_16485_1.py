import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

c, b = map(int, input().split())
print(c / b)