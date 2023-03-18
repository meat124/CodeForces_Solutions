from math import sqrt
import sys
input = sys.stdin.readline
MAX = 4*10**5
sq_list = []
a = 0
# 제곱수 배열 생성
while a*a <= MAX:
    sq_list.append(a*a)
    a += 1


for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    # 연속된 부분 수열의 곱에서 제곱수를 제외한 나머지의 개수를 출력한다.
    j = 0
    cur = 0
    # XOR 연산의 결과가 제곱수인 쌍의 개수
    cnt = 0
    m = [0]*(2*n)
    m[cur] += 1
    while j < n:
        cur ^= A[j]
        # i 는 MAX 까지의 제곱수
        for i in sq_list:
            # 만약 i 가 2*n 보다 크거나 같다면 그 이후는 검사 필요 없으므로 break
            if i >= 2*n:
                break
            # 만약 cur 과 현재 제곱수인 i 를 XOR 한 결과가 2*n 보다 작다면?
            if cur ^ i < 2*n:
                cnt += m[cur ^ i]
        # 현재까지 prefix XOR 인덱스 위치에 값을 하나 올린다.
        m[cur] += 1
        j += 1
    print(n*(n + 1)//2 - cnt)
