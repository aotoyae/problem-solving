import sys
import math
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
tree = int(input())
count = 0
lst = []

for _ in range(n - 1):
    num = int(input())
    lst.append(num - tree)
    tree = num

g = lst[0]

for i in range(1, len(lst)):
    g = math.gcd(g, lst[i])

for v in lst:
    count += v // g - 1

print(count)

