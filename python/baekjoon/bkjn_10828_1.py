import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    order = input().split()

    if order[0] == 'push':
        lst.append(order[1])
    elif order[0] == 'pop':
        if lst:
            num = lst.pop()
            print(num)
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(lst))
    elif order[0] == 'empty':
        print(0) if lst else print(1)
    else:
        print(lst[-1]) if lst else print(-1)


