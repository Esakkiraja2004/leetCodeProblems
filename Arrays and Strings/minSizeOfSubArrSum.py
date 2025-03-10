target = 7 
nums = [2,3,1,2,4,3]

n = len(nums)
l = 0

output = float("inf")

curr_sum = 0

for r in range(n):
    curr_sum += nums[r]
    while curr_sum >= target:
        w = (r-l)+1
        output = min(w,output)
        curr_sum -= nums[l]
        l += 1

print(output)