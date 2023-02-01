import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    result = 0
    weak = h.count(1)
    if weak >= 2:
        result = (weak//2) + (n - weak) + (weak % 2)
    else:
        result = n
    print(result)
