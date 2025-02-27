import sys, math
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

R = int(input())

print(f'{R * R * math.pi:.6f}')
print(f'{2 * R * R:.6f}')