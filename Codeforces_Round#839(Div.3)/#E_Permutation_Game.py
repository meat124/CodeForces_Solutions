import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x, y, z = 0, 0, 0
    for i in range(n):
        asc, des = i + 1, n - i
        if a[i] == asc and a[i] == des:
            continue
        elif a[i] == asc and a[i] != des:
            y += 1
        elif a[i] != asc and a[i] == des:
            x += 1
        else:
            z += 1
    if x + z <= y:
        print('First')
    elif y + z < x:
        print('Second')
    else:
        print('Tie')
