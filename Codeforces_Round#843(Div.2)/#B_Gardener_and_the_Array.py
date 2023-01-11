from collections import Counter
import sys
input = sys.stdin.readline


def Solution():
    n = int(input())
    # 각 비트가 입력된 개수를 저장한다.
    bit_cnt = Counter()
    # 입력을 저장한다.
    arr_c = []
    for i in range(n):
        c_i = list(map(int, input().split()))[1:]
        bit_cnt.update(c_i)
        arr_c.append(c_i)
    # 수열의 각 원소를 확인한다.
    for i in arr_c:
        # 현재 원소의 모든 비트들이 출현한 개수가 unique 하지 않다면 없어져도 or 연산이 동일하게 유지된다.
        if all(bit_cnt[bit] != 1 for bit in i):
            return "YES"
    return "NO"


for t in range(int(input())):
    print(Solution())
