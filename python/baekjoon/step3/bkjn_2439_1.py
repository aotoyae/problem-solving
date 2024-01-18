num = int(input())
result = ""

for i in range(1, num + 1):
  result = " " * (num - i) + "*" * i
  print(result)