import sys
input = sys.stdin.readline
str = 'codeforces'
for t in range(int(input())):
    s = input().rstrip()
    result = 0
    for i, a in enumerate(s):
        if s[i] != str[i]:
            result += 1
    print(result)
