import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
K = bin(N)[2:]
num = 0

for i in range(len(K)):
    if int(K[i]) == 1:
        num += 3 ** (len(K) - i - 1)

print(num)