import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

X = input()

if X[0] == '0':
    if X[1] == 'x':
        print(int(X, 16))
    else:
        print(int(X, 8))
else:
    print(X)