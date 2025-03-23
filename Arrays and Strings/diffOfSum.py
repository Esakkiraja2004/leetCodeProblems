class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = [int(x) for x in str(nums) if x.isdigit()]
        return abs(sum(x) - sum(nums))