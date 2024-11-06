import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

word = input().strip()
words = []

for i in range(len(word) - 2):
    for j in range(i + 1, len(word) - 1):
        for k in range(j + 1, len(word)):
            part = word[:j][::-1] + word[j:k][::-1] + word[k:][::-1]
            words.append(part)

print(min(words))
# print(sorted(words)[0])
