import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
dic = dict()

for _ in range(N):
    word = input().strip()

    if word in dic: dic[word] += 1
    elif len(word) >= M: dic[word] = 1

sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in sorted_dic:
    print(word)
