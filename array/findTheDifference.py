s = "a"
t = "aa"
for i in t:
    if i not in s :
        print(i)
    else:
        if s.count(i) != t.count(i):
            print(i)


