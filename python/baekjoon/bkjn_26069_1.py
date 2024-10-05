import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
dance= {'ChongChong'}

for _ in range(N):
    A, B = input().strip().split()

    if A in dance: dance.add(B)
    elif B in dance: dance.add(A)

print(len(dance))
