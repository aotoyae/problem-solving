def solution(numbers):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i, n in enumerate(num):
        numbers = numbers.replace(n, str(i))

    return int(numbers)