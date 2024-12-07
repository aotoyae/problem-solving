import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

X, Y = input().split()
reversed_X = int(X[::-1])
reversed_Y = int(Y[::-1])


print(int(str(reversed_X + reversed_Y)[::-1]))

