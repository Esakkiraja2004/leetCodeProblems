n = [1,0,2,3,0,4,4]
z= n.count(0)
for i in range(z):
    n.remove(0)
    n.append(0)
print(n)