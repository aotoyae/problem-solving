import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
stack = []
num = 1

for student in lst:
    stack.append(student)

    while stack and stack[-1] == num:
        stack.pop()
        num += 1

if stack: print('Sad')
else: print('Nice')