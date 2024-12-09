import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = [input().split() for _ in range(N)]
sorted_lst = sorted(lst, key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(sorted_lst[-1][0])
print(sorted_lst[0][0])
