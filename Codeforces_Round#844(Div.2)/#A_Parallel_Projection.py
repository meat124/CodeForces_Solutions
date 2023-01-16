import sys
for t in range(int(input())):
    w, d, h = map(int, sys.stdin.readline().split())
    a, b, f, g = map(int, sys.stdin.readline().split())
    print(min(b+g+abs(a-f)+h, (d-b)+(d-g)+abs(a-f)+h,
              a+f+abs(b-g)+h, (w-a)+(w-f)+abs(b-g)+h))
