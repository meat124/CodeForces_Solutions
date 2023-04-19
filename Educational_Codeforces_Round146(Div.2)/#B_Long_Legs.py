import sys
input = sys.stdin.readline

for t in range(int(input())):
    a, b = map(int, input().split())
    result = 10**18
    for i in range(1, 10**5):
        result = min(result, (a + i - 1)//i + (b + i - 1)//i + (i - 1))
    print(result)
