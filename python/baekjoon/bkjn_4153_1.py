import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))
    lst.sort()
    ausar, auset, heru = lst[0], lst[1], lst[2]

    if ausar + auset + heru == 0:
        break

    if heru * heru == ausar * ausar + auset * auset:
        print('right')
    else:
        print('wrong')
