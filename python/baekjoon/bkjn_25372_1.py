N = int(input())

for _ in range(N):
    pw_len = len(input())

    print('yes') if 6 <= pw_len <= 9 else print('no')