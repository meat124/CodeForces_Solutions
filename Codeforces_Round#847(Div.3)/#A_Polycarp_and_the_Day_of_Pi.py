import sys
input = sys.stdin.readline
pi = '314159265358979323846264338327'
for t in range(int(input())):
    n = input().rstrip()
    cnt = 0
    for i in range(len(n)):
        if pi[i] != n[i]:
            break
        cnt += 1
    print(cnt)
