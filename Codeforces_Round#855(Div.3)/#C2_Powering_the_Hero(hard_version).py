import heapq
import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    hero_cnt = 0
    bonus = []
    result = 0
    for i in range(n):
        if s[i] == 0 and len(bonus):
            result += -heapq.heappop(bonus)
        else:
            heapq.heappush(bonus, -s[i])
    print(result)
