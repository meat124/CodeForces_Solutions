import sys
input = sys.stdin.readline


def Solve():
    n, w, h = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 중심의 차이
    # 양수이면 케익 중심이 오른쪽, 음수이면 케익 중심이 왼쪽에 존재
    d = [a[i] - b[i] for i in range(n)]
    return 'YES' if max(d) - min(d) <= (w - h)*2 else 'NO'


for t in range(int(input())):
    print(Solve())
