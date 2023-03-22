import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    B = list(map(int, input().split()))
    liked = len(list(filter(lambda x: x > 0, B)))
    max_liked = list(range(1, liked + 1)) + \
        list(range(liked - 1, liked - 1 - (n - liked), -1))
    rem = n - liked
    common = min(liked, rem)
    min_liked = [1, 0]*common
    liked -= common
    rem -= common
    if liked:
        min_liked += list(range(1, liked + 1))
    else:
        min_liked += [0]*rem
    print(*max_liked)
    print(*min_liked)
