n = [6,2,6,5,1,2]
n.sort()
print(n)
l = len(n)
res =0
for i in range(0 , l , 2):
    res += n[i]
print(res)
