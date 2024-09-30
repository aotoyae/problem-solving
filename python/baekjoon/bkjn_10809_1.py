string = input()
result = []

for i in range(97, 123):
  result.append(string.find(chr(i)))

print(" ".join(map(str, result)))