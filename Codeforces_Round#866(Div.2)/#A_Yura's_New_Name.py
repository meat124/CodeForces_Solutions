import sys
input = sys.stdin.readline
for t in range(int(input())):
    s = input().rstrip()
    result = 0
    if len(s) == 1:
        if s == '^':
            result += 1
            s += '^'
        else:
            s = '^_^'
            result += 2
    if s[0] == '_':
        result += 1
        s = '^' + s
    if s[-1] == '_':
        result += 1
        s = s + '^'
    for i in range(1, len(s) - 2):
        if s[i] == '_' and s[i + 1] == '_':
            result += 1
    print(result)
