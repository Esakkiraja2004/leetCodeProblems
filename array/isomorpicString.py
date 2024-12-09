s= 'ehgjg'
t = 'adbdg'

map1 = []
map2 = []
for idx in s:
    map1.append(s.index(idx))
for idx in t:
    map2.append(t.index(idx))
if map1 == map2:
    print(True) 
else:
    print(False)
print(map1)
print(map2)