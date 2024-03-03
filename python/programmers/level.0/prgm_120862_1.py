def solution(numbers):
    sort_numbers = sorted(numbers)

    return max(sort_numbers[0]*sort_numbers[1], sort_numbers[-1]*sort_numbers[-2])