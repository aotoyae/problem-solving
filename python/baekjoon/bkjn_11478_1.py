import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

word = input().strip()
set_lst = set()

for i in range(len(word)):
    for j in range(i, len(word)):
        set_lst.add(word[i:j + 1])

print(len(set_lst))


