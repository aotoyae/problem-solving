while True:
  num1, num2 = map(int, input().split())
  
  if num1 == 0 and num2 == 0:
    break
  elif num1 % num2 == 0:
    print("multiple")
  elif num2 % num1 == 0:
    print("factor")
  else:
    print("neither")