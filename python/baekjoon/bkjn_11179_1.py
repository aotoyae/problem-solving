import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())

bin_N = bin(N)[2:]
reversed_bin_N = bin_N[::-1]
dec_N = int(reversed_bin_N, 2)

print(dec_N)
