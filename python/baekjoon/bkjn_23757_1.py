import sys, heapq
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
box = []

for i in list(map(int, input().split())):
    heapq.heappush(box, -i)

child = list(map(int, input().split()))

present_is_not_enough = False

for i in child:
    n = -heapq.heappop(box)

    if n - i < 0:
        present_is_not_enough = True
        print(0)
        exit()

    heapq.heappush(box, -(n - i))

print(1)
