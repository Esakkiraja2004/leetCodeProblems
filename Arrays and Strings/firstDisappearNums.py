class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)+1
        nums = set(nums)
        arr =[]
        for i in range(1,n):
            if i not in nums:
                arr.append(i)
        return arr