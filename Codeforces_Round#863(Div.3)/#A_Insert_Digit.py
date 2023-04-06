import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, d = map(int, input().split())
    num = input().rstrip()
    idx = -1
    for i in range(n):
        if int(num[i]) < d:
            idx = i
            break
    print(num[:idx] + str(d) + num[idx:]) if idx != -1 else print(num + str(d))
