def solution(s1, s2):
    count = 0

    if len(s1) >= len(s2):
        long_arr = s1
        short_arr = s2
    else:
        long_arr = s2
        short_arr = s1

    for i in  short_arr:
        if i in long_arr:
            count += 1

    return count
