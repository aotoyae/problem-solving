import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = [0] * 10
num = 1 # 현재 자리수

def make_nine(number):
    while number % 10 != 9:
        for i in str(number):
            lst[int(i)] += num

        number -= 1

    return number

while N > 0:
    N = make_nine(N) # N 을 9로 끝나는 수로 맞춰둔다.

    if N < 10: # N 이 10 보다 작다면 0 ~ N 을 개별적으로 처리
        for i in range(N + 1):
            lst[i] += num
    else: # 10 이상이라면 한 번에 계산
        for i in range(10):
            lst[i] += (N // 10 + 1) * num
    lst[0] -= num # 0 은 현재 자리수에서 등장하지 않으므로 빼준다.
    num *= 10 # 다음 자리수로 이동
    N //= 10 # 다음 자리수 처리 위해 줄임

print(*lst)
