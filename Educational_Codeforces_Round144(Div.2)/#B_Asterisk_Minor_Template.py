import sys
input = sys.stdin.readline

for t in range(int(input())):
    a = input().rstrip()
    b = input().rstrip()
    if a[0] == b[0]:
        print('YES')
        print(a[0] + '*')
    elif a[-1] == b[-1]:
        print('YES')
        print('*' + a[-1])
    else:
        for i in range(len(b) - 1):
            if b[i] + b[i + 1] in a:
                print('YES')
                print('*' + b[i] + b[i + 1] + '*')
                break
        else:
            print('NO')
