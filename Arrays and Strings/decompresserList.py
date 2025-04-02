nums = [1,2,3,4]
arr =[]
for i in range(0 , len(nums),2):
    arr.extend( [nums[i+1]] * nums[i])
print(arr)