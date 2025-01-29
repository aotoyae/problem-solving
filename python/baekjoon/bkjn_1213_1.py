import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

NAME = input().strip()
dic = {}
keys = sorted(list(set(NAME)))
present = ''
odd = []

for key in keys:
    cnt = NAME.count(key)
    dic[key] = cnt
    if cnt % 2:
        odd.append(key)

if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    for k, v in dic.items():
        present += k * (v // 2)

    if odd:
        present += odd[0] + present[::-1]
    else:
        present += present[::-1]

    print(present)


