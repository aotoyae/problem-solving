import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
lst = input().split()
test = input().split()

for food in lst:
    if food not in test:
        print(food)
        break