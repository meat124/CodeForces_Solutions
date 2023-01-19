import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    x = 1
    # cnt : 정렬되지 않은 원소의 개수
    cnt = 0
    for i in p:
        if i != x:
            cnt += 1
        else:
            x += 1
    # 한 번에 k 개씩 정렬 가능하므로 k로 나눈 몫에 나머지를 정렬하기 위한 1을 더한다.
    print((cnt - 1)//k + 1)
