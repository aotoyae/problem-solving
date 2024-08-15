from itertools import combinations

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0

    for n in combinations(nums, 3):
        num = sum(n)
        if is_prime(num):
            answer += 1

    return answer