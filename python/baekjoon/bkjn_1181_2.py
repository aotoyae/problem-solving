import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]
words = list(set(words))

words.sort(key=lambda x: (len(x), x))

for i in words:
    print(i)