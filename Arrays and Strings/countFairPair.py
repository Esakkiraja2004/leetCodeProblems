class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        def lower_bound(nums, target, start):
            low, high = start, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return low

        def upper_bound(nums, target, start):
            low, high = start, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid
            return low

        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n):
            left = lower_bound(nums, lower - nums[i], i + 1)
            right = upper_bound(nums, upper - nums[i], i + 1)
            count += (right - left)

        return count
