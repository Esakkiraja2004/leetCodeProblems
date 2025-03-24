nums = [1,2,3,2]
c = {}
for i in nums:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1 
print(c)

s = 0

for i in c:
    if c[i] == 1:
        s += i
print(s)