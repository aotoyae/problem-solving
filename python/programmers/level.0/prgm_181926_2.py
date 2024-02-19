def solution(n, control):
    obj = { "w":1, "s":-1, "d":10, "a":-10 }
    for i in control:
        n += obj[i]

    return n