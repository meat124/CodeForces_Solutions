from collections import OrderedDict
import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    s = input().rstrip().lower()
    S = []
    for i in s:
        if not S or i != S[-1]:
            S.append(i)
    print('YES') if ''.join(S) == 'meow' else print('NO')
