def solution(quiz):
    result = []
    for q in quiz:
        left, right = q.split(" = ")
        x, operator, y = left.split()
        sum = 0

        if operator == "+":
            sum = int(x) + int(y)
        else:
            sum = int(x) - int(y)
        
        result.append("O") if sum == int(right) else result.append("X")

    return result