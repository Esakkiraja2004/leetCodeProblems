nums = [4,5,6,7,0,1,2]
l = 0 
h = len(nums)-1
m = 0

while l <h :
    m = (high + low) // 2
    if nums[m] < target:
        h = m+1
    elif nums[m] > target :
        h = m-1
    else:
        return m
    return -1
