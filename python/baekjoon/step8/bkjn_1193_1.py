import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

num = int(input())
line = 1

while num > line:
    num -= line
    line += 1

if line % 2 == 0:
    a = num
    b = line - num + 1
else:
    a = line - num + 1
    b = num

print(f'{a}/{b}')

