from collections import Counter
import sys
input = sys.stdin.readline


def Is_Ugly(arr):
    sum = arr[0]
    for i in range(1, len(arr)):
        if sum == arr[i]:
            return True
        sum += arr[i]
    return False


for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if not Is_Ugly(a):
        print('YES')
        print(*a)
        continue
    if len(Counter(a).keys()) == 1:
        print('NO')
        continue
    a.sort(reverse=True)
    if a[0] == a[1]:
        a.insert(0, a.pop())
    print('YES')
    print(*a)
