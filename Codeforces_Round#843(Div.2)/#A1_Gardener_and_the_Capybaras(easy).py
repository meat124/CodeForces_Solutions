import sys
for i in range(int(input())):
    s = sys.stdin.readline().rstrip()
    # b 는 나머지보다 작거나, 또는 나머지보다 커야한다.
    flag = False
    for j in range(1, len(s) - 1):
        for k in range(j + 1, len(s)):
            if (s[:j] >= s[j:k] and s[j:k] <= s[k:]) or (s[:j] <= s[j:k] and s[j:k] >= s[k:]):
                print(f"{s[:j]} {s[j:k]} {s[k:]}")
                flag = True
                break
        if flag:
            break
