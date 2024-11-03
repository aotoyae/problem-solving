import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

ipt = input().split('-')
temp = []

for i in ipt:
    cnt = 0
    for j in i.split('+'):
        cnt += int(j)
    temp.append(cnt)

result = temp[0]
for i in temp[1:]:
    result -= i

print(result)