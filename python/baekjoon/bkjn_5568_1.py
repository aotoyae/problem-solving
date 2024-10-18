from itertools import permutations
import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
k = int(input())
lst = [input().strip() for _ in range(n)]
num_set = set()

for i in permutations(lst, k):
    num_set.add(''.join(i))

print(len(num_set))
