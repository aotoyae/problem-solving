def solution(number, limit, power):
    result = 0

    for i in range(1, number + 1):
        count = 0

        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                if i / j == j: count += 1
                else: count += 2

        if count > limit: count = power
        result += count
    
    return result