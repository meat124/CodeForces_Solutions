import sys
input = sys.stdin.readline
for t in range(int(input())):
    # i,j 번째 원소의 binary representation 에서 b번째 자리의 비트를 서로 swap 한다.
    # 그때 max(a) - min(a) 의 값을 구하여라
    n = int(input())
    A = list(map(int, input().split()))
    B1 = [False]*12
    B0 = [False]*12
    max_len, min_len = 0, 15
    for i in range(n):
        a = bin(A[i])[2:]
        max_len = max(max_len, len(a))
        min_len = min(min_len, len(a))
    for i in range(n):
        a = bin(A[i])[2:]
        for j in range(len(a)):
            idx = max_len - len(a) + j
            if a[j] == '1':
                B1[idx] = True
            if a[j] == '0':
                B0[idx] = True
    max_a, min_a = '', ''
    for i in range(max_len):
        max_a += '1' if B1[i] else '0'
    for i in range(min_len):
        idx = max_len - min_len + i
        min_a += '0' if B0[idx] == True else '1'
    print(int(max_a, 2) - int(min_a, 2))
