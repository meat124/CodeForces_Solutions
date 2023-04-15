import sys
input = sys.stdin.readline
for t in range(int(input())):
    s = input().rstrip()
    if s.count('0') == 0:
        print(len(s)**2)
        continue
    consecutive = 0
    new_s = s + s
    max_len = 0
    cur = 0
    for i in range(len(new_s)):
        if new_s[i] == '1':
            cur += 1
        else:
            cur = 0
        max_len = max(max_len, cur)
    max_len += 1
    print((max_len//2)*(max_len//2 + (max_len % 2)))
