def solution(a, b, n):
    bottle = 0

    while n >= a:
        bottle += (n // a) * b
        n = (n // a) * b + (n % a)

    return bottle