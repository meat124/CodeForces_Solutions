from collections import Counter, deque
import sys
input = sys.stdin.readline
MAX = 2*10**5

for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    # 0 의 개수가 절반 이하이면 최소 MEX 는 0으로 만들 수 있다.
    zero_cnt = A.count(0)
    if zero_cnt <= n//2 + (n % 2):
        print(0)
    else:
        one_cnt = A.count(1)
        new_A = []
        for a in A:
            if a != 0:
                new_A.append(a)
        if len(new_A) == 0:
            print(1)
        elif len(new_A) == one_cnt:
            print(2)
        else:
            print(1)
