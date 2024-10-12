import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

dic = dict()

for i in range(1, 9):
    dic[i] = int(input())

sorted_dic = dict(sorted(dic.items(), key=lambda item:item[1], reverse=True)[:5])

cnt = 0
lst = []

for k, v in sorted_dic.items():
    lst.append(str(k))
    cnt += v

lst.sort()

print(cnt)
print(' '.join(lst))
