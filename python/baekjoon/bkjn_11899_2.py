import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

S = input().strip()

while '()' in S:
    S = S.replace('()', '')

print(len(S))