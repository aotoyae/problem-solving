import sys
import heapq
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if x == 0:
        print(heapq.heappop(heap)[1]) if heap else print(0)
    else:
        heapq.heappush(heap, (abs(x), x))