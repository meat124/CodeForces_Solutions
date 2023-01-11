import sys
s = sys.stdin.readline().rstrip()
alpha = ('h', 'e', 'l', 'l', 'o', 'END')
p = 0
for i in s:
    if i == alpha[p]:
        p += 1
print("YES") if p == 5 else print("NO")
