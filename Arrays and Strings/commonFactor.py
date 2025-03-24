class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        arr =set()
        barr = set()
        for i in range(1,a+1):
            if a % i == 0:
                arr.add(i)
        for i in range(1,b+1):
            if b % i == 0:
                barr.add(i)
        
        new = arr & barr
        return len(new)