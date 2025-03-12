class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        neg = 0

        i = 0

        while i < len(nums):
            if nums[i] < 0:
                neg += 1
            elif nums[i] > 0:
                pos += 1

            i+=1

        return max(pos,neg)