def solution(id_pw, db):
    id, pw = id_pw

    for i in range(len(db)):
        if db[i][0] == id and db[i][1] == pw:
            return "login"        
        if db[i][0] == id and db[i][1] != pw:
            return "wrong pw"        

    return "fail"