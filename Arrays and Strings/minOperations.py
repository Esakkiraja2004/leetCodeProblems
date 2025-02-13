import bisect

def min_operations(nums, k):
    nums.sort()  # Sort initially
    operations = 0

    while nums[0] < k:  # While the smallest element is less than k
        if len(nums) < 2:
            return -1  # Not enough elements to continue

        min_val = nums.pop(0)  # Remove the smallest element
        max_val = nums.pop(0)  # Remove the second smallest element

        new_val = (min_val * 2) + max_val  # Compute new value

        bisect.insort(nums, new_val)  # Insert new value in sorted order
        operations += 1

    return operations

# Example usage
nums = [2, 11, 10, 1, 3]
k = 10
print("Minimum operations:", min_operations(nums, k))  # Output: 2
