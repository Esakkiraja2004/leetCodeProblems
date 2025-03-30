nums = [1,2,4]
m = 0
arr = nums + [nums[0]]

for i in range(len(arr)):
    z = abs(arr[i-1] - arr[i])
    m = max(m , z)
print(m)