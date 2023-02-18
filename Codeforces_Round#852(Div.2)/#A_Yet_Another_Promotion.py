import sys
input = sys.stdin.readline

for t in range(int(input())):
    a, b = map(int, input().split())
    n, m = map(int, input().split())
    result = 0
    # 만약 프로모션보다 사야할 개수가 적다면
    if n < m + 1:
        result = min(a*m, a*n, b*n)
    # 만약 프로모션이 더 싸다면?
    elif a*m < b*(m + 1):
        promotion = n//(m + 1)
        result += m*a*promotion + (n - (m + 1)*promotion)*min(a, b)
    else:
        result += min(a, b)*n
    print(result)
