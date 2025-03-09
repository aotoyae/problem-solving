import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

K = int(input())
D1, D2 = map(int, input().split())

H = K ** 2 - ((D1 - D2) / 2) ** 2
print(H)