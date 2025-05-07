import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

jh = input()
doctor = input()

if len(jh) >= len(doctor):
    print('go')
else:
    print('no')