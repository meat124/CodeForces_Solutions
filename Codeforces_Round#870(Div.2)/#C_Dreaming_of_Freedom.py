import sys
input = sys.stdin.readline
MAX = 10**6 + 100
min_div = [0]*MAX
for d in range(2, MAX):
    if min_div[d] == 0:
        min_div[d] = d
        for i in range(d*d, MAX, d):
            if min_div[i] == 0:
                min_div[i] = d
for i in range(1, MAX):
    if min_div[i] == 0:
        min_div[i] = i


for t in range(int(input())):
    n, m = map(int, input().split())
    print('YES') if n == 1 or min_div[n] > m else print('NO')
