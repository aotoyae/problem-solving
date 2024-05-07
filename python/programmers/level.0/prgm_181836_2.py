def solution(picture, k):
    result = []

    for i in range(len(picture)):
        result += [picture[i].replace('.', '.' * k).replace('x', 'x' * k)] * k