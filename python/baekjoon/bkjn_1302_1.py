import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
dic = {}

for _ in range(N):
    book = input().strip()

    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1

sorted_dic = dict(sorted(dic.items(), key=lambda x: (x[1], x[0])))
max_key = max(sorted_dic, key=sorted_dic.get)
print(max_key)