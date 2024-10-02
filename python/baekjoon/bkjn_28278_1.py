import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    command = input().split()

    if command[0] == "1":
        lst.append(command[1])
    elif command[0] == "2":
        if lst:
            print(lst.pop())
        else:
            print(-1)
    elif command[0] == "3":
        print(len(lst))
    elif command[0] == "4":
        print(0) if lst else print(1)
    elif command[0] == "5":
        print(lst[-1]) if lst else print(-1)

