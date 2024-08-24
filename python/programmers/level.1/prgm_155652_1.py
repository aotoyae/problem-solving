def solution(s, skip, index):
    answer = ""

    for i in s:
        code = ord(i)

        for j in range(index):
            code += 1
            if code > 122: code = 97

            while chr(code) in skip:
                code += 1
                if code > 122: code = 97

        answer += chr(code)

    return answer