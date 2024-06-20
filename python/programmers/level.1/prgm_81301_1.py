def solution(s):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(len(num)):
        arr = s.split(num[i])
        s = str(i).join(arr)

    return int(s)