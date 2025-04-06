import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = input().split()
    lst_A = sorted(list(A))
    lst_B = sorted(list(B))

    if lst_A == lst_B:
        print(f"{A} & {B} are anagrams.")
    else:
        print(f"{A} & {B} are NOT anagrams.")