class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m = 0
        for i in accounts:
            x = sum(i)
            m = max(m,x)
        return m
        