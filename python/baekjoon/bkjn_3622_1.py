import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

A, a, B, b, P = map(int, input().split())

if A > P or B > P:
    print('No')
elif A + B <= P or a >= B or b >= A:
    print('Yes')
else:
    print('No')
