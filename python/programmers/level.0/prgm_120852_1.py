def solution(n):
    result = []
    i = 2

    while n >= 2:
        if n%i == 0:
            n /= i
            if i not in result:
                result.append(i)
        else:  i += 1

    return result