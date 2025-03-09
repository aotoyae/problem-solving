import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
answer = round((T / 2) ** 2)

print(answer)
