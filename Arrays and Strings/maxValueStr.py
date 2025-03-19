strs = ["1","01","001","0001"]
m = 0
for i in strs:
    if i.isdigit():
        z = int(i)
        m = max(z,m)
    else:
        z  = len(i)
        m = max(m,z)
print(m)