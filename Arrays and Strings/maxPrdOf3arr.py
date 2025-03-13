nums = [1,2,3,4]
nums.sort(reverse= True)
max1 = nums[0] * nums[1] * nums[2]
max2 = nums[-1] * nums[-2] * nums[0]
print(max(max1 , max2))