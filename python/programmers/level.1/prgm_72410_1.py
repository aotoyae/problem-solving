def solution(new_id):
    new_id = new_id.lower()
    result = ''

    for i in new_id:
        if i.isalnum() or i in '-_.':
            result += i

    while '..' in result:
        result = result.replace('..', '.')

    if result[0] == '.' and len(result) > 1: result = result[1:]
    if result[-1] == '.': result = result[:-1]
    if result == '': result = 'a'

    if len(result) >= 16:
        result = result[:15]
        if result[-1] == '.': result = result[:-1]

    if len(result) <= 2:
        result += result[-1] * (3 - len(result))

    print(result)

solution('...!@BaT#*..y.abcdefghijklm')