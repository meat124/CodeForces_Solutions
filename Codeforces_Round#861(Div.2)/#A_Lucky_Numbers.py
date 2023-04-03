import sys
input = sys.stdin.readline


def Get_max_gap(n):
    st, en = 9, 0
    n = str(n)
    for i in n:
        st = min(st, int(i))
        en = max(en, int(i))
    return en - st


for t in range(int(input())):
    l, r = map(int, input().split())
    result = None
    if r - l < 100:
        gap = 0
        for i in range(l, r + 1):
            tmp = Get_max_gap(i)
            if gap <= tmp:
                result = i
                gap = tmp
    else:
        for i in range(l, r + 1):
            if i % 100 == 90:
                result = i
                break
    print(result)
