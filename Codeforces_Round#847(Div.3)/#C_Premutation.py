import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    seq = [[*map(int, input().split())] for i in range(n)]
    result = []
    for i in range(1, n - 1):
        if seq[i - 1][0] == seq[i][0] == seq[i + 1][0]:
            continue
        elif seq[i - 1][0] == seq[i][0]:
            result.append(seq[i][0])
            result += seq[i + 1]
            break
        elif seq[i - 1][0] == seq[i + 1][0]:
            result.append(seq[i - 1][0])
            result += seq[i]
            break
        else:
            result.append(seq[i + 1][0])
            result += seq[i - 1]
            break
    print(*result)
