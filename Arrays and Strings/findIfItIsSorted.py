nums = [8,4,2,30,15]
for i in range(len(nums)):
    for j in range(i+1 , len(nums)):
        if bin(nums[i]) > bin(nums[j]):
            nums[i], nums[j] = nums[j], nums[i]   
print(nums)
