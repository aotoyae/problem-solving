def solution(myString):
    arr = myString.split("x")
    return [len(i) for i in arr]