class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        arr = []
        for i in image:
            i.reverse()
            arr.append([x ^ 1 for x in i])
        return arr