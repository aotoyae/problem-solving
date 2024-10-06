import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ps = input()
    lst = []

    for i in ps:
        if i == '(': lst.append(i)
        elif i == ')':
            if lst:
                lst.pop()
            else:
                print('NO')
                break

    else: print('YES') if not lst else print('NO')