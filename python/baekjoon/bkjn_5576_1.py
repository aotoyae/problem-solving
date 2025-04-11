import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

W = []
K = []

for _ in range(10):
    W.append(int(input()))

for _ in range(10):
    K.append(int(input()))

W_total = sum(sorted(W, reverse=True)[:3])
K_total = sum(sorted(K, reverse=True)[:3])

print(W_total, K_total)