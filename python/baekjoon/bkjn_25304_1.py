total_price = int(input())
total_type = int(input())

add_price = 0

for i in range(total_type):
  price, number = map(int, input().split())
  add_price += price * number

if total_price == add_price:
  print("Yes")
else:
  print("No")