import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

x, y, w, h = map(int, input().split())
sm = min(w - x, h - y, x, y)

print(sm)