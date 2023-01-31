import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # 홀*3 or 짝2홀1
    odd, even = [], []
    for i in range(n):
        if a[i] & 1:
            odd.append(i + 1)
        else:
            even.append(i + 1)
    if len(odd) >= 3:
        print('YES')
        print(*odd[:3])
    elif len(odd) == 2 and len(even) == 1:
        print('NO')
    elif len(odd) == 2 and len(even) >= 2:
        print('YES')
        print(odd[0], *even[:2])
    elif len(odd) == 1:
        print('YES')
        print(odd[0], *even[:2])
    else:
        print('NO')
