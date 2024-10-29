import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

word = input().strip()
bomb = input().strip()
bomb_len = len(bomb)
stk = []

for i in word:
    stk.append(i)

    if ''.join(stk[-bomb_len:]) == bomb:
        del stk[-bomb_len:]

print(''.join(stk)) if stk else print('FRULA')