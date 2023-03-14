import sys
input = sys.stdin.readline
S = 'FBFFBFFBFBFFBFFBFBFFBFFB'

for t in range(int(input())):
    k = int(input())
    s = input().rstrip()
    print('YES') if s in S else print('NO')
