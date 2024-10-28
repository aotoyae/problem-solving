# import sys
# sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

while True:
    sentence = input()
    stk = []

    if sentence == '.':
        break

    for i in sentence:
        if i == '[' or i == '(':
            stk.append(i)
        elif i == ']':
            if len(stk) != 0 and stk[-1] == '[':
                stk.pop()
            else:
                stk.append(i)
                break
        elif i == ')':
            if len(stk) != 0 and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(i)
                break

    if len(stk) == 0:
        print('yes')
    else:
        print('no')