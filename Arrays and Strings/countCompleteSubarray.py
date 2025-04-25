class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(set(nums))
        res = 0
        for i in range(len(nums)):
            s = set()
            for j in range(i,len(nums)):
                s.add(nums[j])
                if len(s) == k:
                    res += 1
        return res