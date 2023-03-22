import sys
input = sys.stdin.readline

for t in range(int(input())):
    a, b, c = map(int, input().split())
    print('+') if a + b == c else print('-')
