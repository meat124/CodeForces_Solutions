import sys
X, Y, Z = 0, 0, 0
for i in range(int(input())):
    x, y, z = map(int, sys.stdin.readline().split())
    X += x
    Y += y
    Z += z
print("YES") if X == 0 and Y == 0 and Z == 0 else print("NO")
