import queue
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        karan = queue.PriorityQueue()
        score = 0
        for i in range(len(nums)):
            karan.put((-nums[i]))
        for i in range(k):
            h = -1 * karan.get()
            score += h
            h = ceil(h/3)
            karan.put(-h)
        return score