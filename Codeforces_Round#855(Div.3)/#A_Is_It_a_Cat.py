from collections import Counter
import sys
input = sys.stdin.readline
result = {'M': 'MmEe', 'm': 'MmEe', 'E': 'EeOo', 'e': 'EeOo',
          'O': 'OoWw', 'o': 'OoWw', 'W': 'Ww', 'w': 'Ww'}

for t in range(int(input())):
    n = int(input())
    s = input().rstrip()
    if n < 4:
        print('NO')
        continue
    s_keys = Counter(s).keys()
    r = 'YES'
    for i in range(n - 1):
        if s[i] not in 'MmEeOoWw':
            r = 'NO'
            break
        if s[i + 1] in result[s[i]]:
            continue
        else:
            r = 'NO'
            break
    if not (s[0] in 'Mm' and s[-1] in 'Ww'):
        r = 'NO'
    print(r)
