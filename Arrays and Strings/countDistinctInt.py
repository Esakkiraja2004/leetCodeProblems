nums = [1,13,10,12,31]
for i in range(len(nums)):
    z = str(nums[i])
    nums.append(int(z[::-1]))
print(len(set(nums)))