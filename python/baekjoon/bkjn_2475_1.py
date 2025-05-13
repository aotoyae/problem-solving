import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

lst = list(map(int, input().split()))
lst2 = [i * i for i in lst]

print(sum(lst2) % 10)