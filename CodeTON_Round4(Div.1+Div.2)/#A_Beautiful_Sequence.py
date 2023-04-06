import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    A = [10**9] + list(map(int, input().split()))
    result = 'NO'
    for i in range(n + 1):
        if i >= A[i]:
            result = 'YES'
            break
    print(result)
