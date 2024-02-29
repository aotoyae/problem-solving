def solution(myString):
    return ''.join([i.lower() if i != 'a' and i != 'A' else i.upper() for i in myString])