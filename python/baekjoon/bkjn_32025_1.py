import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

H = int(input())
W = int(input())
sm = min(H, W)

print(int(sm * 0.5 * 100))