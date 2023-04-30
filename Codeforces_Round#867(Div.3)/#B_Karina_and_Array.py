import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    a_fir, a_sec, b_fir, b_sec = None, None, None, None
    for i in range(n):
        if a_fir == None or A[i] > a_fir:
            a_sec = a_fir
            a_fir = A[i]
        elif a_sec == None or A[i] > a_sec:
            a_sec = A[i]
        if b_fir == None or A[i] < b_fir:
            b_sec = b_fir
            b_fir = A[i]
        elif b_sec == None or A[i] < b_sec:
            b_sec = A[i]
    print(max(a_fir*a_sec, b_fir*b_sec))
