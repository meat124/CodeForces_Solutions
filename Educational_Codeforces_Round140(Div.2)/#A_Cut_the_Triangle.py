import sys


def Is_Straight(p1, p2):
    if p1[0] == p2[0] or p1[1] == p2[1]:
        return 1
    return 0


for t in range(int(input())):
    input()
    tri = []
    for i in range(3):
        x, y = map(int, input().split())
        tri.append([x, y])
    cnt = Is_Straight(tri[0], tri[1]) + Is_Straight(tri[0],
                                                    tri[2]) + Is_Straight(tri[1], tri[2])
    if cnt >= 2:
        print('NO')
    else:
        print('YES')
