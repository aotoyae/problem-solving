import sys
import math
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
lst = [0] * n

count_of_squares = int(math.sqrt(n))

print(count_of_squares)
