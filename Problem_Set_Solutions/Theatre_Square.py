n, m, a = map(int, input().split())
row, col = (n//a) + 1 if n % a else (n//a), (m//a) + 1 if m % a else (m//a)
print(row*col)
