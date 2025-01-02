import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
recommend = int(input())
number = list(map(int, input().split()))
dic = {}

for i in number:
    if i in dic:
        dic[i] += 1
    else:
        if len(dic) >= N:
            key_to_pop = min(dic, key=lambda k: (dic[k]))
            dic.pop(key_to_pop)

        dic[i] = 1

print(*sorted(dic.keys()))