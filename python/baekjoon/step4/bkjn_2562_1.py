arr = []
for i in range(9):
  i = int(input())
  arr.append(i)

print(max(arr), arr.index(max(arr)) + 1, sep="\n")