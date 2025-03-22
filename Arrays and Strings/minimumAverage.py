nums = [7,8,3,4,15,13,4,1]
avg = []
nums.sort()

while nums:
    minimum = nums[0]
    maximum = nums[len(nums)-1]
    val = (minimum + maximum) / 2
    avg.append(val)
    nums.remove(minimum)
    nums.remove(maximum)
print(min(avg))