import sys
input = sys.stdin.readline
MAX = 10**5

for t in range(int(input())):
    # 사람수, 친구가 아닌 쌍의 개수
    n, m = map(int, input().split())
    min_limit_friend = [n]*n
    for i in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if x > y:
            x, y = y, x
        min_limit_friend[x] = min(min_limit_friend[x], y)

    for i in range(n - 2, -1, -1):
        min_limit_friend[i] = min(min_limit_friend[i], min_limit_friend[i + 1])
    result = 0
    for i in range(n):
        result += min_limit_friend[i] - i
    print(result)
