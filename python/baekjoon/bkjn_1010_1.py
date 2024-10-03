import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def factorial(n):
    num = 1

    for i in range(1, n + 1):
        num *= i

    return num

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    bridge = factorial(M) // (factorial(M - N) * factorial(N))
    print(bridge)

