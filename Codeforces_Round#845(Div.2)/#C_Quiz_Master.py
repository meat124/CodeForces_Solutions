import sys
input = sys.stdin.readline
MAX = int(1e5 + 1)
factors = [[] for i in range(MAX)]
# factors[3] = [1,3]
# factors[12] = [1,2,3,4,6,12]
# factors[x] : x의 약수들을 저장한다.
for i in range(1, MAX):
    for j in range(i, MAX, i):
        factors[j].append(i)


for t in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # smartness 오름차순 정렬
    a.sort()
    # 약수가 등장한 횟수를 저장
    div_cnt = [0]*(m + 1)
    # topic을 정복한 횟수, 결과
    topics, begin, result = 0, 0, MAX
    for i in range(n):
        for factor in factors[a[i]]:
            # 약수가 m(topics) 보다 작거나 같은 경우에만 시행
            if factor <= m:
                div_cnt[factor] += 1
                # 만약 처음 체크가 되었다면 topic 을 새롭게 정복한 것이므로 +1
                if div_cnt[factor] == 1:
                    topics += 1
        # 1~m 까지 모든 topic 을 정복한 경우 계속 시행
        while topics == m:
            # 최솟값으로 갱신
            result = min(result, a[i] - a[begin])
            # a[begin] 이 가지고 있는 topic 을 제거하기 위한 코드
            for factor in factors[a[begin]]:
                # 약수가 m 보다 작거나 같은 경우만 시행
                if factor <= m:
                    div_cnt[factor] -= 1
                    # 만약 약수가 등장한 횟수가 0이 되었다면 topics 을 1 감소시키고 탈출
                    if div_cnt[factor] == 0:
                        topics -= 1
            # 문제 없다면 다음 begin 으로 넘어감
            begin += 1
    print(result) if result != MAX else print(-1)
