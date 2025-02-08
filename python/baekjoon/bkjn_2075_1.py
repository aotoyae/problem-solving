import sys, heapq
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    nums = map(int, input().split())

    for n in nums:
        if len(hq) < N:
            heapq.heappush(hq, n)
        else:
            if hq[0] < n:
                heapq.heappop(hq)
                heapq.heappush(hq, n)

print(hq[0])
