import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

print(board) if 'X' not in board else print(-1)
