import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, s, r = map(int, input().split())
    max_v = s - r
    seq = [max_v]
    base = r // (n - 1)
    for i in range(n - 1):
        seq.append(base)
    for i in range(r - base*(n - 1)):
        seq[n - 1 - i] += 1
    print(*seq)
