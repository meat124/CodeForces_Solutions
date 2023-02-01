import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    # n^2 - 1 이 가장 크고
    # 1이 가장 작은 차이이다.
    # 즉, 1~n^2-1 까지 모두 등장해야한다.
    matrix = [0]*n
    st, en = 1, n**2
    # 가장 큰 차이부터 시작해서 점점 줄여나가면 된다.(그리디)
    flag = True
    for i in range(n):
        for j in range(n):
            # st를 사용하면 그 다음은 en 을 사용하고, en 을 사용하면 그 다음은 st 를 사용하는 식으로 진행한다.
            if flag:
                matrix[j] = st
                flag = False
                st += 1
            else:
                matrix[j] = en
                flag = True
                en -= 1
        # 홀수번 행이면 역순으로 출력하고, 아니면 그대로 출력
        print(*(matrix[::-1] if i & 1 else matrix))
