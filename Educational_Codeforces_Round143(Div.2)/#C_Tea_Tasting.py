import sys
from bisect import bisect_right
input = sys.stdin.readline
N = 2*10**5 + 5

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    prefix_b = [0]
    for i in range(n):
        prefix_b.append(prefix_b[-1] + b[i])
    cnt = [0]*(n + 1)
    drink_amount = [0]*(n + 1)
    # i 번째 티를 순서대로 taster 들에게 먹이고, 마지막 taster 가 있다면 남은걸 다 먹인다.
    for i in range(n):
        en = bisect_right(prefix_b, prefix_b[i] + a[i]) - 1
        # cnt[i]~cnt[en] 까지 모두 1을 더하려면 TLE 가 발생하므로
        # 앞과 뒤만 조정하고 나머지는 drink_amount를 결정할 때 같이 시행한다.
        # 즉, 여기서부터 증가한다는 표시만 하는 셈
        cnt[i] += 1
        cnt[en] -= 1
        drink_amount[en] += a[i] - (prefix_b[en] - prefix_b[i])
    for i in range(n):
        drink_amount[i] += cnt[i]*b[i]
        # 앞에서 마신 횟수를 뒤에서도 인정해서 더해준다.
        cnt[i + 1] += cnt[i]
    print(*drink_amount[:n])
