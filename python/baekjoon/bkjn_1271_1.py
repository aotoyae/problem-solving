import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n, m = map(int, input().split())

print(n // m)
print(n % m)