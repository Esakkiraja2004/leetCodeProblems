nums = [1,2,3,4]
m = 0
n = len(nums)
for i in range(n):
    if n % (i+1) == 0:
        print(i)
        m += nums[i] * nums[i]
print(m)