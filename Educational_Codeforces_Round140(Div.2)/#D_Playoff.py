import sys
input = sys.stdin.readline
n = int(input())
s = list(input().rstrip())
x = s.count('0')
y = n - x
print(*list(range(2**y, 2**n - 2**x + 2)))
