import sys
input = sys.stdin.readline

for t in range(int(input())):
    s = input().rstrip()
    result = 'YES'
    if len(s) == 1 and s not in 'Yes':
        result = 'NO'
    for i in range(len(s) - 1):
        if s[i] == 'Y':
            if s[i + 1] != 'e':
                result = 'NO'
                break
        elif s[i] == 'e':
            if s[i + 1] != 's':
                result = 'NO'
                break
        elif s[i] == 's':
            if s[i + 1] != 'Y':
                result = 'NO'
                break
        else:
            result = 'NO'
            break
    print(result)
