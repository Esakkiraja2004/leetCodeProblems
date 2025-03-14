nums = [1,2,3,1,1,3]
res = []
for i in range(len(nums)):
    for j in range(i+1 , len(nums)):
        if nums[i] == nums[j] and i <j:
            res.append((i,j))
print(res)