class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        c = 0
        a = sorted(heights)
        for i in range(len(a)):
            if heights[i] != a[i]:
                c += 1
        return c