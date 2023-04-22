from collections import Counter
import sys
input = sys.stdin.readline
for t in range(int(input())):
    s = input().rstrip()
    cnt = Counter(s)
    result = 2*10**5
    for a in cnt.keys():
        st = 0
        tmp = 0
        idx = -1
        for i in range(len(s)):
            if s[i] == a:
                tmp = max(tmp, i - st)
                st = i + 1
                idx = i
        tmp = max(tmp, len(s) - 1 - idx)
        tmp_ = 0
        while tmp != 0:
            tmp //= 2
            tmp_ += 1
        result = min(result, tmp_)
    print(result)
