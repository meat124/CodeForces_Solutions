import sys
input = sys.stdin.readline


for t in range(int(input())):
    a = list(map(int, input().split()))
    print(a[0] + 2*min(a[1:3]) + min(a[0] + 1, abs(a[1] - a[2]) + a[3])
          ) if a[0] != 0 else print(1)
