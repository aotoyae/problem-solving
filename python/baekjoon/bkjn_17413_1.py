import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

S = input().strip() + ' '
stack = []
result = ''
check = False

for i in S:
    if i == '<':
        check = True

        for _ in range(len(stack)):
            result += stack.pop()

    stack.append(i)

    if i == '>':
        check = False

        for _ in range(len(stack)):
            result += stack.pop(0)

    if i == ' ' and check == False:
        stack.pop()

        for _ in range(len(stack)):
            result += stack.pop()

        result += ' '

print(result)
