import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    # 홀수 인덱스 요소들의 합과 짝수 인덱스 요소들의 합의 차이
    gap_sum = 0
    for i in range(n):
        gap_sum += A[i] if i & 1 else -A[i]
    # n 이 홀수면 무조건 가능하다
    # 또는 홀수 인덱스 요소들이 합이 짝수 인덱스 요소들의 합보다 크거나 같다면 가능하다.
    print('YES') if n & 1 or gap_sum >= 0 else print('NO')
