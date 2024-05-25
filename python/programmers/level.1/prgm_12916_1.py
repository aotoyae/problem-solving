def solution(s):
    s_up = s.upper()
    p_len = 0
    y_len = 0

    for i in s_up:
        if i == "P": p_len += 1
        if i == "Y": y_len += 1

    return p_len == y_len

