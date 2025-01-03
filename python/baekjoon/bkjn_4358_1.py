import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

dic = {}
total = 0

while True:
    tree = input().strip()

    if tree == '':
        break

    total += 1

    if tree in dic:
        dic[tree] += 1
    else:
        dic[tree] = 1

sorted_dic = dict(sorted(dic.items()))

for key, value in sorted_dic.items():
    per = value / total * 100

    print("%s %.4f" % (key, per))