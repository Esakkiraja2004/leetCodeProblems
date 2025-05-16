class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        d ={}
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        for i in s1:
            if i in d:
                d[i] += 1
            else:
                d[i] =1
        for i in s2:
            if i in d:
                d[i] += 1
            else:
                d[i] =1
        return [key for key , values in  d.items() if values == 1]
                
        