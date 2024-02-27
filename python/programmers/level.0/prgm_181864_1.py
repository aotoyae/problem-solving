def solution(myString, pat):
    new_string = ''
    
    for i in myString:
        new_string += 'B' if i == 'A' else 'A'
    
    return int(pat in new_string)