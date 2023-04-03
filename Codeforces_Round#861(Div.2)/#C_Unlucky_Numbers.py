import sys
input = sys.stdin.readline


def Diff(x):
    return int(max(str(x))) - int(min(str(x)))


for t in range(int(input())):
    l, r = input().rstrip().split()
    if l == r:
        print(l)
        continue
    if len(l) != len(r):
        print('9'*min(len(l), len(r)))
    else:
        result = l
        i = 0
        # 공통인 접두사는 일단 포함
        while i < len(l) and l[i] == r[i]:
            i += 1
        gap = Diff(l)
        if i < len(l):
            for x in range(int(l[i]), int(r[i]) + 1):
                for y in range(10):
                    tmp = l[:i] + str(x) + str(y)*(len(r) - i - 1)
                    if l <= tmp <= r and Diff(tmp) < gap:
                        result = tmp
                        gap = Diff(tmp)
        print(result)
