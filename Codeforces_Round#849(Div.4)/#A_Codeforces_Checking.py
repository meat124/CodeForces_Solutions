import sys
input = sys.stdin.readline

for t in range(int(input())):
    c = input().rstrip()
    if c in 'codeforces':
        print('YES')
    else:
        print('NO')
