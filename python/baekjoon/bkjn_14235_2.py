import sys
import heapq
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
    place = list(map(int, input().split()))

    if place[0] == 0:
        if queue:
            present = -heapq.heappop(queue)
            print(present)
        else:
            print(-1)
    else:
        for i in range(place[0]):
            heapq.heappush(queue, -place[i + 1])
