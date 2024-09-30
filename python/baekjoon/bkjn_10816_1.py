import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
my_cards = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))
dic = {}
lst = []

for my_card in my_cards:
    if my_card in dic:
        dic[my_card] += 1
    else:
        dic[my_card] = 1

for card in cards:
    if card in dic:
        lst.append(dic[card])
    else:
        lst.append(0)

print(" ".join(map(str, lst)))
