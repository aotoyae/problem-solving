def solution(s, n):
    answer = ""

    for i in s:
        if i == " ": answer += " "
        else:
            code = ord(i)
            if code <= 90:
                code += n
                if code > 90: code -= 26
            else:
                code += n
                if code > 122: code -= 26
            answer += chr(code)

    return answer
