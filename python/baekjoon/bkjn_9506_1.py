while True:
  num = int(input())
  num_list = []

  if num == -1:
    break
  
  for i in range(1, num // 2 + 1):
    if num % i == 0:
      num_list.append(i)
  
  if num == sum(num_list):
    print(f"{num} =", " + ".join(map(str, num_list)))
  else:
    print(f"{num} is NOT perfect.")
