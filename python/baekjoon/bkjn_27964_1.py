import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
lst = input().split()
cheese_set = set()

for cheese in lst:
    if cheese.endswith("Cheese"):
        cheese_set.add(cheese)

if len(cheese_set) >= 4:
    print('yummy')
else:
    print('sad')