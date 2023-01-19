from collections import Counter
import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # 두 개의 순열 p,q 에서 max(p_i, q_i) = a_i 인 수열을 구하여라
    cnt = Counter(a)
    # 만약 같은 값이 2개 초과하면 2개의 순열로 만들 수 없다.
    flag = False
    if max(cnt.values()) > 2:
        print('NO')
        continue
    for i in cnt.keys():
        if cnt[i] > i:
            flag = True
            break
    if flag:
        print('NO')
        continue
    # a에서 사용되지 않은 수
    not_appear = sorted(list(set(range(1, n + 1)) - set(a)))
    p, q = [0]*n, [0]*n
    p_vis, q_vis = [False]*(n + 1), [False]*(n + 1)
    # 2개 등장하는 번호들을 저장한다.
    second_appear = sorted(list(i for i in cnt.keys() if cnt[i] == 2))
    s_a = {}
    if len(not_appear) < len(second_appear):
        flag = True
    else:
        for i in range(len(not_appear)):
            if not_appear[i] < second_appear[i]:
                s_a[second_appear[i]] = not_appear[i]
            else:
                flag = True
    if flag:
        print('NO')
        continue
    for i in range(n):
        # 1개 출현하는 번호는 같은 위치에 배치해서 해결
        # 2개 출현하는 번호는? >> p,q에 돌아가면서 배치하고, 그 수보다 작은 수를 하나 구해야한다.
        # 그때 a에 등장하지 않은 번호를 사용한다.
        if cnt[a[i]] == 1:
            p[i], q[i] = a[i], a[i]
        # 2개 출현하는 번호
        else:
            if p_vis[a[i]]:
                q[i] = a[i]
                p[i] = s_a[a[i]]
                q_vis[a[i]] = True
            else:
                p[i] = a[i]
                q[i] = s_a[a[i]]
                p_vis[a[i]] = True
    print('YES')
    print(*p)
    print(*q)
