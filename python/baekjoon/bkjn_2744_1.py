import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

word = input()

for i in word:
    if i.isupper():
        i = i.lower()
    else:
        i = i.upper()

    print(i, end='')