import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    s = input().rstrip()
    flag = False
    idx = 0
    for i in range(1, n):
        if s[i] <= s[0]:
            flag = True
            if s[idx] >= s[i]:
                idx = i
    print(s[idx] + s[:idx] + s[idx + 1:]) if flag else print(s)
