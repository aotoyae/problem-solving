import sys

total = int(input())
num = 1
for i in range(total):
  a, b = map(int, sys.stdin.readline().split())
  print(f"Case #{num}: {a} + {b} = {a + b}")
  num +=1