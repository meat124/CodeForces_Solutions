vowels = ('a', 'e', 'i', 'o', 'u', 'y')
s = filter(lambda x: x not in vowels, input().lower())
print('.'+".".join(s))
