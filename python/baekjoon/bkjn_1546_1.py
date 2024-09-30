num = int(input())
scores = list(map(int, input().split(" ")))
max = max(scores)
average = 0 

for i in range(num):
  average += scores[i] / max * 100

print(average / num)