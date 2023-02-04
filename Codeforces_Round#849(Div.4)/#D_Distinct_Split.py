from collections import Counter
import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    s = input().rstrip()
    f_a, f_b = Counter(), Counter(list(s))
    result = len(f_b)
    for c in s:
        if c in f_a:
            f_a[c] += 1
        else:
            f_a[c] = 0
        f_b[c] -= 1
        if f_b[c] == 0:
            f_b.pop(c)
        result = max(result, len(f_a) + len(f_b))
    print(result)
