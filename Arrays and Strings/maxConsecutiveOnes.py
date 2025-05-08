nums = [1,1,0,1,1,1]
c = 0
m = 0

for i in nums:
    if i == 1:
        c += 1
        m = max(c,m)
    else:
        c = 0
print(m)