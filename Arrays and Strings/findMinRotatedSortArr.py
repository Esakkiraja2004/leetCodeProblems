nums = [3,4,5,1,2]
a = sorted(nums)
c =1
for i in range(1,len(nums)):
    if nums[i] < nums[i-1]:
        c+=1
        nums[i] , nums[i-1] = nums[i-1] , nums[i]
print(min(a))