def solution(s):
    answer  = []

    for i in s:
        if s.index(i) == s.rindex(i):
            answer.append(i)

    return ''.join(sorted(answer))