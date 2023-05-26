import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    L = list(map(int, input().split()))
    result = -1
    for i in range(n + 1):
        liars = 0
        for j in L:
            if j > i:
                liars += 1
        if liars == i:
            result = liars
            break
    print(result)
