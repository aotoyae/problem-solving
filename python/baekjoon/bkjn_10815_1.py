import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
my_cards = set(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))
lst = []

for card in cards:
    lst.append(1) if card in my_cards else lst.append(0)

print(" ".join(map(str, lst)))
