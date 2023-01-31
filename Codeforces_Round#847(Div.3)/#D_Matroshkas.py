from collections import Counter
import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a_counter = Counter(a)
    result = 0
    cnt = 1
    for i in range(n - 1):
        if a[i] + 1 < a[i + 1]:
            result += cnt
            cnt = 1
        elif a[i] == a[i + 1]:
            cnt = max(cnt, a_counter[a[i]])
        elif cnt > a_counter[a[i]]:
            result += (cnt - a_counter[a[i]])
            cnt = a_counter[a[i]]
    result += cnt
    print(result)
