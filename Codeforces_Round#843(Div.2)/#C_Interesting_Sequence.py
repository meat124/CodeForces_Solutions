import sys


def Solution():
    n, x = map(int, sys.stdin.readline().split())
    if n == x:
        return n
    # res : 누적해서 AND 연산을 진행한 값을 저장하는 변수
    # cur : 현재 값
    res, cur = n, n
    for i in range(len(bin(n)) - 2):
        # cur 에서 처음으로 1비트가 나온다면
        if (cur >> i) & 1:
            # 그 비트에 1을 더해줘서 다음 비트를 1로 만든다.
            cur += (1 << i)
        # 누적 AND 연산을 진행한다.
        res &= cur
        # 만약 x와 같아졌다면 cur 값이 M 값이다.
        if res == x:
            return cur
    return -1


for t in range(int(input())):
    print(Solution())
