import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

y = (c * d - a * f) // (b * d - a * e)
x = (b * f - c * e) // (b * d - a * e)

print(x, y)