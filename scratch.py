d = {'a' : 1, 'b' : 2, 'c' : 3}
for letter in d.values():
    print(letter, d[letter])

print(d.get('d', 'LOOOOOL'))