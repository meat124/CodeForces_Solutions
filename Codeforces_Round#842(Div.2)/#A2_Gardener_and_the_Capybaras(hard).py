import sys
for t in range(int(input())):
    s = sys.stdin.readline().rstrip()
    if s[1] == 'a':
        print(s[0], s[1], s[2:])
    else:
        print(s[0], s[1:-1], s[-1])
