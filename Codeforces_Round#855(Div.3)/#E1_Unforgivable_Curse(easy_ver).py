import sys
input = sys.stdin.readline


def Solve():
    n, k = map(int, input().split())
    s = input().rstrip()
    t = input().rstrip()
    # cnt 배열이 의미하는 것?
    # 만약 s 에 속한 문자의 개수와, t 에 속한 문자의 개수가 서로 다르다면 아무리 swap 을 시행해도
    # 절대 s to t 를 할 수 없다.
    # 따라서 s 에 속하는 문자의 인덱스를 1증가시키고
    # t 에 속하는 문자의 인덱스를 1 감소시켜서 진행하면
    # 만약 최종적으로 모든 원소가 0이라면 문자의 개수가 서로 같은 것이고
    # 만약 하나라도 0이 아닌 것이 존재한다면 문자의 개수가 서로 다른 것이다.
    cnt = [0]*26
    ok = True
    for i in range(n):
        # 만약 변경할 수 있는 범위 안에 있다면
        if i >= k or i + k < n:
            # 기존 문자의 개수를 하나 늘리고
            cnt[ord(s[i]) - ord('a')] += 1
            # 최종 문자열의 그 문자를 하나 감소시킨다?
            cnt[ord(t[i]) - ord('a')] -= 1
        # 만약 범위 밖에 있다면?
        # 만약 두 문자가 같고 ok = True 이라면 True
        # ok = False 라면 False
        # 만약 두 문자가 다르고 ok = True 이라면 False
        # ok = False 라면 True
        # else 로 넘어오는 조건은 현재 인덱스 i 가 k 구역 내에 바꿀 수 있는 문자가 없는 경우이다.
        # 즉 스왑이 불가능한 상황에서 두 문자가 서로 다르다면 s to t 가 불가능하다.
        else:
            ok &= s[i] == t[i]
    # ok = True 이고, cnt 배열의 모든 원소가 0이라면 YES 출력, 아니면 NO 출력
    return 'YES' if ok and cnt.count(0) == 26 else 'NO'


for t in range(int(input())):
    print(Solve())
