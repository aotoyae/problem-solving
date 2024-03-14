def solution(my_string, s, e):
    start = my_string[:s]
    s_e = my_string[s:e+1]
    reverse = s_e[::-1]
    end = my_string[e+1:]

    return start + reverse + end