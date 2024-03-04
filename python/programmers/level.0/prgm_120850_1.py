def solution(my_string):
    answer = [i for i in my_string if i.isdigit()]
    return sorted(answer)