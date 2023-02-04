import sys
input = sys.stdin.readline
d = {'L': [-1, 0], 'R': [1, 0], 'U': [0, 1], 'D': [0, -1]}

for t in range(int(input())):
    n = int(input())
    s = input().rstrip()
    coord = [0, 0]
    flag = False
    for c in s:
        coord[0] += d[c][0]
        coord[1] += d[c][1]
        if coord == [1, 1]:
            flag = True
            break
    print('YES') if flag else print('NO')
