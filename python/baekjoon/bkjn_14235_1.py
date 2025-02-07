import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
    place = input().strip()

    if place == '0':
        if queue:
            present = max(queue)
            print(present)
            queue.remove(present)
        else:
            print(-1)
    else:
        lst = list(map(int, place.split()))
        lst.pop(0)
        queue += lst
