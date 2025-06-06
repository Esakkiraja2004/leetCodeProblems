class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        low = 0
        high = len(letters) - 1

        while low <= high:
            mid = (low + high) // 2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        
        if low == len(letters):
            return letters[0]
        return letters[low]
