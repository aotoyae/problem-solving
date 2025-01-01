import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())

def isPrime(x):
    if x == 1:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True

def isPalindrome(x):
    str_x = str(x)
    if str_x == str_x[::-1]:
        return True
    return False

while True:
    if isPrime(N) and isPalindrome(N):
        print(N)
        break

    N += 1
