import sys
input = sys.stdin.readline
MAX = 50005
last = [0]*MAX

for t in range(int(input())):
    m = int(input())
    # last[i] : i 번 사람이 마지막으로 축제에 참가한 날짜
    A_ = []
    for i in range(m):
        n_i = int(input())
        A = list(map(int, input().split()))
        A_.append(A)
        for a in A:
            last[a] = i
    result = [-1]*m
    for i in range(m):
        for j in A_[i]:
            if last[j] == i:
                result[i] = j
        if result[i] == -1:
            print(-1)
            break
    else:
        print(*result)
