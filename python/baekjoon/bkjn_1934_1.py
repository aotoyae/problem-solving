import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
from math import gcd

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    lcm = A * B // gcd(A, B)
    print(lcm)