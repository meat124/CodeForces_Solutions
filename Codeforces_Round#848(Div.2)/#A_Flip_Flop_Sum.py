import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    if -1 not in a:
        print(sum_a - 4)
    else:
        flag = False
        for i in range(n - 1):
            if a[i] == -1 and a[i + 1] == -1:
                flag = True
        if flag:
            print(sum_a + 4)
        # -1이 연속으로 없다면 그냥 출력
        else:
            print(sum_a)
