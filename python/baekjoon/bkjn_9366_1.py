import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())

for i in range(T):
    lst = sorted(map(int, input().split()))
    a, b, c = lst[0], lst[1], lst[2]

    print(f"Case #{i + 1}: ", end="")

    if a + b <= c:
        print("invalid!")
    elif a == b == c:
        print("equilateral")
    elif a == b or a == c or b == c:
        print("isosceles")
    else:
        print("scalene")