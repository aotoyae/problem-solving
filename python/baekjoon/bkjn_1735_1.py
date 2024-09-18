import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def solution(x, y):
    while y:
        mod = y
        y = x % y
        x = mod
    return x

a, b = map(int, input().split())
c, d = map(int, input().split())

e, f = a * d + c * b, b * d

n = solution(e, f)

print(e // n, f // n)