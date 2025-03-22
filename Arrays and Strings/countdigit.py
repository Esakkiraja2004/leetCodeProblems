class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        l = [int(x) for x in str(num)]
        c = 0
        for i in l:
            if num % i == 0:
                c+=1
        return c 
