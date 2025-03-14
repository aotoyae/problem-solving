import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

D, H, W = map(int, input().split())
R = D / (H ** 2 + W ** 2) ** 0.5
height = int(H * R)
width = int(W * R)

print(height, width)