s = "abacbc"
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(len(set(d.values())) ==  1)