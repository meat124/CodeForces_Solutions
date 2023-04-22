import sys
input = sys.stdin.readline
for t in range(int(input())):
    s = input().rstrip()
    digit = s.count('?')
    if digit == 0:
        print('0') if s[0] == '0' else print('1')
        continue
    if s[0] == '0':
        print('0')
        continue
    print(10**digit) if s[0] != '?' else print(9*10**(digit - 1))
