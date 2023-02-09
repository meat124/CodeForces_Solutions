import sys
input = sys.stdin.readline
for t in range(int(input())):
    a = list(sorted(map(int, input().split())))
    print(a[1])
