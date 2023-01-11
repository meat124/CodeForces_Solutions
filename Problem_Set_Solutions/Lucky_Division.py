ln = (4, 7, 44, 47, 77, 444, 447, 474, 477, 744, 747, 774, 777)
n = int(input())
flag = False
for i in ln:
    if n % i == 0:
        flag = True
print("YES") if flag else print("NO")
