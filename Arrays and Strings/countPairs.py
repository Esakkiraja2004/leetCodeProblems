c = 0
nums = [1,2,3,4,5,6]
for i in range(len(nums)):
    for j in range(i+1 , len(nums)):
        if nums[i] + nums[j] < target:
            c+= 1
print(c)