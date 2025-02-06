nums = [3,6 , 9, 1]
nums.sort()
value =  [] 
if len(nums) < 2:
    print(0)
for i in range(1,len(nums)):
    value.append(nums[i] - nums[i-1])
print(max(value))