n = 2
b = []
for i in range(0,n+1):
    b.append(bin(i).replace("b","0"))

res =[]

for i in b:
    res.append(i.count("1"))

print(res)