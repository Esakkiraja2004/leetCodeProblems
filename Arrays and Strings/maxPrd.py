class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                n = (nums[i]-1) * (nums[j]-1)
                m = max(n,m)
        return m