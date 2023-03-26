import sys
input = sys.stdin.readline

for t in range(int(input())):
    s = input().rstrip()
    S = set()
    for i in s:
        S.add(i)
    if len(S) >= 3:
        print(4)
    elif len(S) == 2:
        # 만약 1:3 이면
        print(6) if s.count(s[0]) == 1 or s.count(s[0]) == 3 else print(4)
    else:
        print(-1)
