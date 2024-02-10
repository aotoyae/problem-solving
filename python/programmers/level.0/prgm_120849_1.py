def solution(my_string):
    test = ["a", "e", "i", "o", "u"]
    for word in test:
        my_string = my_string.replace(word, "")

    return my_string