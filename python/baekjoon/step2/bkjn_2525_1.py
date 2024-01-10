hour, minute = map(int, input().split())
timer = int(input())

hour += timer // 60
minute += timer % 60

if minute >= 60:
  minute -= 60
  hour += 1
if hour >= 24:
  hour -= 24

print(hour, minute)