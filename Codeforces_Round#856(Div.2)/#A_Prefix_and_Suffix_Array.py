import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    S = list(input().rstrip().split())
    S.sort(key=len)
    print('YES') if S[-1] == ''.join(reversed(S[-2])) else print('NO')
