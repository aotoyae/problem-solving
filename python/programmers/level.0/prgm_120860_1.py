def solution(dots):
    list = sorted(dots)

    side1= abs(list[0][1] - list[1][1])
    side2= abs(list[0][0] - list[2][0])

    return side1 * side2
