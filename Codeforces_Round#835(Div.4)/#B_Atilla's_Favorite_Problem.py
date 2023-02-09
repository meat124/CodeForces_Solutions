import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    s = input().rstrip()
    print(ord(max(s)) - ord('a') + 1)
