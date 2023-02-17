import sys
input = sys.stdin.readline
MOD = 10**9 + 7
N = 3001
n = int(input())
x = list(map(int, input().split()))
# 점이 p 개 있을 때 그 점들의 이동 방향 조합의 수는 2^p 와 같다.
power = [2**i % MOD for i in range(N)]

result = 0
for i in range(n - 1):
    l, r = i, i
    # j 는 i + 1 부터 시작해서 n 까지 늘어남
    for j in range(i + 1, n):
        while l > 0 and x[l - 1] - x[i] >= x[i] - x[j]:
            l -= 1
        while r < n and x[r] - x[j] < x[j] - x[i]:
            r += 1
        # n - (r - l) >> l~r 간격 이외에 개수
        result += power[n - r + l]
        result %= MOD
print(result)
