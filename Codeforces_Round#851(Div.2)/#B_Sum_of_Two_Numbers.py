import sys
input = sys.stdin.readline
mem = {}


def digit_sum(x):
    ret = 0
    for i in x:
        ret += int(i)
    return ret


for t in range(int(input())):
    n = input().rstrip()
    a = int(n)//2
    b = int(n) - a
    if n in mem:
        print(*mem[n])
    elif len(n) >= 2 and n[-1] == '9' and int(n[-2]) & 1:
        while abs(digit_sum(str(a)) - digit_sum(str(b))) > 1:
            a += 5
            b -= 5
        print(a, b)
        mem[n] = [a, b]
    else:
        print(a, b)
