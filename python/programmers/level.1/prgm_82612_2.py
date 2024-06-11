def solution(price, money, count):
    n_price = 0
    
    for i in range(1, count + 1):
        n_price += i * price
    
    return n_price - money if money < n_price else 0