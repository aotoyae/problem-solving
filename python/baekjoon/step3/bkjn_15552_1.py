import sys

total = int(input())
for i in range(total):
  a, b = map(int, sys.stdin.readline().split())
  print(a + b)