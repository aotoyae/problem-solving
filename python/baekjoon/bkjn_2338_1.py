import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

A = int(input())
B = int(input())

print(A + B, A - B, A * B, sep='\n')