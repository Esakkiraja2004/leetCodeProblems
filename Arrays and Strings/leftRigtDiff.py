nums = [10, 4, 8, 3]
left = []
right = []
final = []

# Calculate left sum (excluding current)
sum_val = 0
for i in range(len(nums)):
    left.append(sum_val)
    sum_val += nums[i]

# Calculate right sum (excluding current)
sum_val = 0
for i in range(len(nums) - 1, -1, -1):
    right.insert(0, sum_val)   # insert at front instead of reversing later
    sum_val += nums[i]

# Find absolute difference
for i in range(len(nums)):
    final.append(abs(left[i] - right[i]))

print(final)
