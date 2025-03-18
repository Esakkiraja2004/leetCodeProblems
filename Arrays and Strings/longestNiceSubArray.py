nums = [3,1,5,11,13]
l = 0
m = 1
for r in range(1, len(nums)):
    while any(nums[r] & nums[i] != 0 for i in range(l ,r)):
        l+=1
    w = (r -l) +1
    m = max(w,m)
print(m)