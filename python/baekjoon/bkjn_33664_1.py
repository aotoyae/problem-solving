B, N, M = map(int, input().split())
dic = dict()
total = 0

for _ in range(N):
    item, price = input().split()
    dic[item] = int(price)

for _ in range(M):
    present = input()
    total += dic[present]

print('acceptable') if total <= B else print('unacceptable')
