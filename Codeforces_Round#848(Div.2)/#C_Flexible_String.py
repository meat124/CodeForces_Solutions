from collections import Counter
import itertools
import sys
input = sys.stdin.readline


for t in range(int(input())):
    n, k = map(int, input().split())
    a = input().rstrip()
    b = input().rstrip()
    # k번 a의 문자를 바꿔서 b와 최장 공통 문자열을 만들어라
    # 그런데 Q 는 set 이므로 만약 같은 문자를 교체할 경우에는 k 의 횟수가 소모되지 않는다.
    keys = Counter(a).keys()
    combs = itertools.combinations(
        keys, min(k, len(keys)))
    max_pairs = 0
    for comb in combs:
        Q = [False]*26
        for c in comb:
            Q[ord(c) - ord('a')] = True
        total, cur = 0, 0
        for i in range(n):
            if a[i] == b[i] or Q[ord(a[i]) - ord('a')]:
                cur += 1
            else:
                cur = 0
            total += cur
        max_pairs = max(max_pairs, total)
    print(max_pairs)
    # 최대 문자가 10개 이므로 10C5 = 252 최악의 경우이다.
    # k == 5 일 때 최악의 경우 가정,
    # valid pairs 는 최장 공통 문자열의 길이가 L 일 때, sum(1toL) 이다.
