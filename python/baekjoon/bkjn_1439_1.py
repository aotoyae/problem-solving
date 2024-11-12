import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

cards = input()
cnt_zero = 0
cnt_one = 0
now = None

for i in cards:
    if i == "0" and now != "0":
        cnt_zero += 1
    elif i == "1" and now != "1":
        cnt_one += 1

    now = i

print(min(cnt_zero, cnt_one))