import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    s = input().rstrip()
    result = n - 1
    for i in range(n - 2):
        prev, nxt = s[i:i+2], s[i+1:i+3]
        if prev[0] == nxt[1]:
            result -= 1
    print(result)
