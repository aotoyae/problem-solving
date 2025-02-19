import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

first = int(input())
second = int(input())
third = int(input())
total = first + second + third

if total == 180:
    if first == second == third:
        print('Equilateral')
    elif first != second and first != third and second != third:
        print('Scalene')
    else:
        print('Isosceles')
else:
    print('Error')