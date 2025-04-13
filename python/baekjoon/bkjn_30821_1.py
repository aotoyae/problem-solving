import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())

def facto(n):
    if n == 1 or n == 0:
        return 1

    return n * facto(n - 1)

print(facto(N) // (facto(N - 5) * facto(5)))