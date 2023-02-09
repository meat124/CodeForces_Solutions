import sys
input = sys.stdin.readline
MAX = int(10**9 + 5)


def Is_Valley(l, r):
    if a[l - 1] > a[l] and a[r] < a[r + 1]:
        return True
    return False


for t in range(int(input())):
    n = int(input())
    a = [MAX] + list(map(int, input().split())) + [MAX]
    l, r = 1, 1
    cnt = 0
    while True:
        if l > n and r > n:
            break
        if a[l] == a[r + 1]:
            r += 1
            continue
        if Is_Valley(l, r):
            cnt += 1
        l = r + 1
        r = l
    print('YES') if cnt == 1 else print('NO')
