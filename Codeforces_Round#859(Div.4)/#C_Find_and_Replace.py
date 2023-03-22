from string import ascii_lowercase
import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    s = input().rstrip()
    L = dict.fromkeys(list(ascii_lowercase))
    result = 'YES'
    L[s[0]] = 1
    for i in range(1, n):
        if L[s[i]] == None:
            L[s[i]] = 1 if L[s[i - 1]] == 0 else 0
        elif L[s[i]] == L[s[i - 1]]:
            result = 'NO'
            break
    print(result)
