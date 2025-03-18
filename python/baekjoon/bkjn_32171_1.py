import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
a, b, c, d = map(int, input().split())
print((c - a + d - b) * 2)

for _ in range(N - 1):
    new_a, new_b, new_c, new_d = map(int, input().split())

    a, b, c, d = min(a, new_a), min(b, new_b), max(c, new_c), max(d, new_d)
    perimeter = (c - a + d - b) * 2
    print(perimeter)
