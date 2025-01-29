import sys
import collections
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

NAME = input().strip()
dic = collections.Counter(NAME)
present = ''
odd_cnt = 0
odd = ''

for k, v in list(dic.items()):
    if v % 2:
        odd_cnt += 1
        odd = k

        if odd_cnt > 1:
            print("I'm Sorry Hansoo")
            quit()

for k, v in sorted(dic.items()):
    present += k * (v // 2)

present += odd + present[::-1]
print(present)
