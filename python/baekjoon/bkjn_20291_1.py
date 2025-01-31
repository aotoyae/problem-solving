import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
dic = {}

for _ in range(N):
    name, extension = input().strip().split(".")

    if extension in dic:
        dic[extension] += 1
    else:
        dic[extension] = 1

for k, v in sorted(dic.items()):
    print(k, v)