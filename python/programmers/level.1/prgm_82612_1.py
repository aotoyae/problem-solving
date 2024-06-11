def solution(price, money, count):
    n_price = 0
    
    for i in range(1, count + 1):
        n_price += i * price
    
    answer = money - n_price
    return abs(answer) if answer < 0 else 0