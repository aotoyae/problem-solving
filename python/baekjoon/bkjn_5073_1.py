import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))
    lst.sort()
    a, b, c = lst[0], lst[1], lst[2]

    if a == b == c == 0:
        break
    elif c >= a + b:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif (a == b and a != c) or (a == c and a != b) or (b == c and a != b):
        print('Isosceles')
    elif a != b != c:
        print('Scalene')