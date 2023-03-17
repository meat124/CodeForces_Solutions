import sys
input = sys.stdin.readline

for t in range(int(input())):
    # 환자수,백신개수,백신유효시간,환자최대대기시간
    n, k, d, w = map(int, input().split())
    T = list(map(int, input().split()))
    T.reverse()
    result = 0
    while T:
        # 첫 환자 입장시간 초기화
        first_patient = T.pop()
        max_time = first_patient + w + d
        cur_cnt = 1
        result += 1
        # T 가 비었거나 현재 환자가 백신의 개수를
        while cur_cnt < k:
            if len(T) == 0:
                break
            if T[-1] > max_time:
                break
            T.pop()
            cur_cnt += 1
    print(result)
