nums = [0,0,1,1,1,1,2,3,3]
l = 0
r = 0

while r < len(nums):
    c = 1
    while r+1 < len(nums)  and nums[r] == nums[r+1]:
        r += 1
        c += 1
    for i in range(min(2,c)):
        nums[l] = nums[r]
        l += 1
    r += 1
print(nums)


