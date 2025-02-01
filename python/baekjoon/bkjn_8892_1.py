import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())

def palindrome():
    N = int(input())
    lst = [input().strip() for _ in range(N)]

    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                word = lst[i] + lst[j]

                if word == word[::-1]:
                    return word

    return 0

while T > 0:
    num = palindrome()

    print(num) if num else print(0)

    T -= 1