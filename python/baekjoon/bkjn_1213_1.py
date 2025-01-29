import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

NAME = input().strip()
dic = {}
present = ''
odd = []

for i in NAME:
    dic[i] = dic.get(i, 0) + 1

for k, v in dic.items():
    if v % 2:
        odd.append(k)

if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    for k, v in sorted(dic.items()):
        present += k * (v // 2)

    present += (odd[0] if odd else '') + present[::-1]

    print(present)
