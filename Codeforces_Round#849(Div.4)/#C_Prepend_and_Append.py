import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    s = input().rstrip()
    st, en = 0, n - 1
    while st <= en and s[st] != s[en]:
        st += 1
        en -= 1
    print(en - st + 1)
