import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

a, b = map(int, input().split())

def solution(a, b):
    while b:
        mod = b
        b = a % b
        a = mod
    return a

print(a * b // solution(a, b))