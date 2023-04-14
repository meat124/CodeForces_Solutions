import sys
input = sys.stdin.readline

for t in range(int(input())):
    k = int(input())
    digits = []
    while k:
        digits.append(k % 9)
        k //= 9
    digits.reverse()
    for i in range(len(digits)):
        if digits[i] >= 4:
            digits[i] += 1
    print(''.join(map(str, digits)))
