n, m = map(int, input().split())
baskets = [0] * n

for i in range(m):
  start, end, ball = map(int, input().split())
  for j in range(start, end + 1):
    baskets[j - 1] = ball

print(*baskets)

