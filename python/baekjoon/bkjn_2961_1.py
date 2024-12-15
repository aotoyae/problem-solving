import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
sour = []
bitter = []

for _ in range(N):
    s, b = map(int, input().split())
    sour.append(s)
    bitter.append(b)

diff = float('inf')

for i in range(1, N + 1):
    lst = list(combinations(list(range(N)), i))

    for food in lst:
        s = 1
        b = 0

        for j in range(i):
            s *= sour[food[j]]
            b += bitter[food[j]]

        if abs(s - b) < diff:
            diff = abs(s - b)

print(diff)
