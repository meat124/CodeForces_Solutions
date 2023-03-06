from collections import Counter
from string import ascii_lowercase, ascii_uppercase

import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, k = map(int, input().split())
    s = input().rstrip()
    letters = Counter(s)
    result = 0
    can_change = 0
    for i in range(26):
        a, b = letters[ascii_lowercase[i]], letters[ascii_uppercase[i]]
        m = min(a, b)
        result += m
        a -= m
        b -= m
        can_change += (a + b)//2
    print(result + min(can_change, k))
