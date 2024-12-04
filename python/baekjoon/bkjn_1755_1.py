import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

M, N = map(int, input().split())
dic = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}
reversed_dict = {v: k for k, v in dic.items()}

lst = []

for i in range(M, N + 1):
    s = ' '.join([dic[n] for n in str(i)])
    lst.append([i, s])

lst.sort(key=lambda x:x[1])

for i in range(len(lst)):
    if i % 10 == 0 and i != 0:
        print()

    print(lst[i][0], end=' ')
