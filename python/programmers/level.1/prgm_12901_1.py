from datetime import date

def solution(a, b):
    week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

    day = date(2016, a, b)
    return week[day.weekday()]