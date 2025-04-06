import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

years = []
names = []

for _ in range(3):
    P, Y, S = input().split()
    years.append(int(Y))
    names.append([int(P), S])

years.sort()
names.sort(reverse=True)

years_name = ''
names_name = ''

for i in range(3):
    years_name += str(years[i] % 100)
    names_name += names[i][1][0]

print(years_name)
print(names_name)