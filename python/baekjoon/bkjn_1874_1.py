import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
stack = []
lst = []
cur = 1

for i in range(n):
    num = int(input())

    while cur <= num:
        stack.append(cur)
        lst.append("+")
        cur += 1

    if stack[-1] == num:
        stack.pop()
        lst.append("-")
    else:
        print("NO")
        exit()

print(*lst, sep='\n')
