def solution(n):
    number = n ** 0.5

    return (number+1)*(number+1) if int(number) == number else -1