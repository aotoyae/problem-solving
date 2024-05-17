def solution(quiz):
    result = []
    for q in quiz:
        x, operator, y, equal, z = q.split(" ")
        sum = 0

        if operator == "+":
            sum = int(x) + int(y)
        else:
            sum = int(x) - int(y)
        
        result.append("O") if sum == int(z) else result.append("X")

    return result