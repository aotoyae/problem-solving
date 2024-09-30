n, x = map(int, input().split())
arr = list(map(int, input().split()))
filtered_arr = filter(lambda num: num < x, arr)

for num in filtered_arr:
  print(num, end=" ")