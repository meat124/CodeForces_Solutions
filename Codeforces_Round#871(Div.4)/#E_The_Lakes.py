from collections import deque
import sys
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def OOB(x,y):
    if x >= n or x < 0 or y >= m or y < 0:
        return True
    return False


def bfs(x,y):
    D = deque()
    D.append([x,y])

    depth = 0

    while D:
        cur_x, cur_y = D.popleft()
        if OOB(cur_x, cur_y):
            continue
        if lake[cur_x][cur_y] == 0 or vis[cur_x][cur_y]:
            continue

        depth += lake[cur_x][cur_y]
        vis[cur_x][cur_y] = True

        for i in range(4):
            nxt_x = cur_x + dx[i]
            nxt_y = cur_y + dy[i]
            if OOB(nxt_x, nxt_y):
                continue
            if lake[nxt_x][nxt_y] == 0 or vis[nxt_x][nxt_y]:
                continue
            D.append([nxt_x, nxt_y])
    return depth



for t in range(int(input())):
    n, m = map(int, input().split())
    vis = [[False] * m for i in range(n)]
    lake = [list(map(int, input().split())) for i in range(n)]
    max_depth = 0
    for i in range(n):
        for j in range(m):
            if lake[i][j] != 0 and not vis[i][j]:
                max_depth = max(max_depth, bfs(i,j))
    print(max_depth)