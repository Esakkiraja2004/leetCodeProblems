class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            m = len(nums) // 2
            left = self.sortColors(nums[:m])
            right = self.sortColors(nums[m:])

            merged = self.merge(left, right)

            # ✅ Copy back to nums to do in-place sorting
            for i in range(len(nums)):
                nums[i] = merged[i]

            return nums  # Still return to be used in recursion
        return nums

    def merge(self, left, right):
        mer = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                mer.append(left[i])
                i += 1
            else:
                mer.append(right[j])
                j += 1

        mer.extend(left[i:])
        mer.extend(right[j:])

        return mer
