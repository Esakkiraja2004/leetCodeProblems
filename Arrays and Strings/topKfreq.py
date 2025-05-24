nums = [1,1,1,2,2,3]
k = 2
d ={}
for i in nums:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
s = sorted(d , key= lambda x : d[x] , reverse= True )
print(s[:k])