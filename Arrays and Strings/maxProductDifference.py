nums = [5,6,2,7,4]
nums.sort()
ans = abs((nums[0] * nums[1]) - (nums[len(nums)-1] * nums[len(nums)-2]))
print(ans)