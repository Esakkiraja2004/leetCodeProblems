nums = [5, 7, 7, 8, 8, 10]
target = 8
arr = []

# Find the first occurrence
def findFirst(nums, target):
    l, r = 0, len(nums) - 1
    res = -1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            res = m
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return res

# Find the last occurrence
def findLast(nums, target):
    l, r = 0, len(nums) - 1
    res = -1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            res = m
            l = m + 1
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return res

first = findFirst(nums, target)
last = findLast(nums, target)

if first != -1:
    arr = list(range(first, last + 1))

print(arr)  # Output: [3, 4]
