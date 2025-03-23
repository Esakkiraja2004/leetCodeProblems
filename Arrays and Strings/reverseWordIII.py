class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split(" ")
        res = []
        for  i in arr:
            res.append(i[::-1])
        return " ".join(res)