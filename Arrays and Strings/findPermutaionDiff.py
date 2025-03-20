class Solution:
    def findPermutationDifference(self, s, t):
        s1, t1 = {}, {}
        n = len(s)
        for i in range(n):
            s1[s[i]] = i
            t1[t[i]] = i
        ans = 0
        for char, index in s1.items():
            ans += abs(index - t1[char])
        return ans
