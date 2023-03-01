import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    s = list(input().rstrip())
    cnt = 0
    i = 0
    while i < n//2:
        tmp = i
        flag = False
        while s[tmp] != s[n - tmp - 1]:
            flag = True
            tmp += 1
            if tmp > n//2 - 1:
                break
        if flag:
            i = tmp - 1
            cnt += 1
        i += 1
    print('YES') if cnt <= 1 else print('NO')
