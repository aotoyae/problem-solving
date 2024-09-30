hour, minute = map(int, input().split())

if minute < 45:
  minute += 60
  if hour == 0:
    hour = 23
  else :
    hour -= 1

print(f"{hour} {minute - 45}")