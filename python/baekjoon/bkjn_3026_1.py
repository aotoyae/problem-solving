import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
rings = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for i in range(1, N):
    g = gcd(rings[0], rings[i])

    print(f"{rings[0] // g}/{rings[i] // g}")