import sys
input = sys.stdin.readline
for t in range(int(input())):
    # n : 몬스터 수, k : 시작 데미지
    n, k = map(int, input().split())
    # 몬스터 체력
    H = list(map(int, input().split()))
    # 몬스터 파워
    P = list(map(int, input().split()))
    # 매 공격 후, 파워가 가장 약한 몬스터의 파워만큼 k(데미지) 가 감소한다.
    # 인덱스 기준으로 정렬을 수행한다.
    # enumerated 의 객체가 전달되고, 그 곳에서 x의 1번째 원소로 key정렬을 수행한다.
    sorted_P = sorted(enumerate(P), key=lambda x: x[1])
    # power 기준으로 정렬된 인덱스스
    I = []
    for idx, val in sorted_P:
        I.append(idx)
    prefix_dmg = 0
    flag = True
    for i in I:
        # 만약 현재 H 가 누적된 데미지의 합 보다 작거나 같다면 이미 죽은 몬스터이므로 넘어간다.
        if H[i] <= prefix_dmg:
            continue
        # 만약 처음이 아니라면 k 를 깎는다.
        if i != I[0]:
            k -= P[i]
        # 아직 데미지가 양수라면 시행한다.
        if k > 0:
            # 누적 데미지에 현재 데미지를 더한다.
            prefix_dmg += k
            # 현재 몬스터의 체력이 누적합보다 크다면 계속 반복한다.
            while H[i] > prefix_dmg:
                # 현재 데미지에서 현재 몬스터 파워의 최솟값을 뺀다.
                k -= P[i]
                # 만약 현재 데미지가 음수가 되면 break
                if k < 0:
                    break
                prefix_dmg += k
        # 만약 현재 몬스터의 체력이 누적 데미지보다 크다면?
        if H[i] > prefix_dmg:
            flag = False
            break
    print('YES') if flag else print('NO')
