import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, TYPE = input().split()
dic = {'Y': 1, 'F': 2, 'O': 3}
people = set()

for _ in range(int(N)):
    people.add(input().strip())

print(len(people) // dic[TYPE])