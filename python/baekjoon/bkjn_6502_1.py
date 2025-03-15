import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

i = 1

while True:
    case = input().strip()

    if case == '0':
        break

    r, w, l = map(int, case.split())
    d = (w ** 2 + l ** 2) ** 0.5

    if r * 2 >= d:
        print(f"Pizza {i} fits on the table.")
    else:
        print(f"Pizza {i} does not fit on the table.")

    i += 1
