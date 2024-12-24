import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
queries = []

for i in range(T):
    k = int(input())
    n = int(input())
    queries.append((k, n))

max_floor = max(q[0] for q in queries)
max_room = max(q[1] for q in queries)

floor = [[i for i in range(1, max_room + 1)]]

for i in range(1, max_floor + 1):
    new_floor = [1]


    for j in range(1, max_room):
        new_floor.append(new_floor[-1] + floor[i - 1][j])

    floor.append(new_floor)

for k, n in queries:
    print(floor[k][n - 1])
