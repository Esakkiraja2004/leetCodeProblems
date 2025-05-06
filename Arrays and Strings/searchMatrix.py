class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for inner in matrix:
            l = 0
            e = len(inner)-1
            while l <= e:
                m = (l+e) // 2
                if inner[m] == target:
                    return True
                elif inner[m] > target:
                    e = m-1
                else:
                    l = m+1
        return False