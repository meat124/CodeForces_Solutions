import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # 음수의 개수가 짝수이면 전부 양수로 변환 가능
    # 만약 음수의 개수가 홀수이면 가장 절대값이 작은 것만 음수로 놔두고
    # 나머지는 양수로 변환 가능
    result = 0
    if len(list(filter(lambda x: x < 0, a))) & 1:
        abs_min = int(1e9 + 5)
        for i in a:
            result += abs(i)
            abs_min = min(abs_min, abs(i))
        result -= 2*abs_min
    else:
        for i in a:
            result += abs(i)
    print(result)
