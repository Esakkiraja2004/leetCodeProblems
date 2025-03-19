class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        while n > 1:
            if n % 2 == 0:
                num += n / 2
                n /= 2
            else:
                num += (n-1) /2
                n = (n-1) / 2 + 1
        return num