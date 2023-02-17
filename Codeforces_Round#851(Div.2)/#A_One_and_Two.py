import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    st, en = 0, a.count(2)
    result = -1
    for i in range(n):
        if a[i] == 2:
            st += 1
            en -= 1
        if st == en:
            result = i + 1
            break
    print(result)
