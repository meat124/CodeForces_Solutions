import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    sqrt_n = int(n**0.5)
    print(sqrt_n - 1) if sqrt_n**2 >= n else print(sqrt_n)
