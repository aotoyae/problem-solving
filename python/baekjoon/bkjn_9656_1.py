import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())

if N % 2 == 1:
    print('CY')
else:
    print('SK')