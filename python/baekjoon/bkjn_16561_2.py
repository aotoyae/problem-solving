import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input()) // 3
cnt = 0

for i in range(1, n - 1):
    cnt += i
    
print(cnt)