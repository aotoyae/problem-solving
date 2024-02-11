def solution(my_string):
    number = 0
    for i in my_string:
        if i.isdigit():
            number += int(i)
    
    return number