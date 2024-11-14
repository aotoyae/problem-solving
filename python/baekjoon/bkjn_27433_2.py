import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())

def recursion(num):
    if num <= 1: # num 이 1 이하이거나 1이라면 바로 1 반환
        return 1
    return num * recursion(num - 1) # 5 * 4 * 3 * 2 * 1, -1 씩 하면서 재귀호출

print(recursion(N))