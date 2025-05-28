class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_index = {c: i for i, c in enumerate(s)}
        seen = []
        in_seen = set()

        for i, c in enumerate(s):
            if c in in_seen:
                continue

            while seen and c < seen[-1] and i < last_index[seen[-1]]:
                in_seen.remove(seen.pop())

            seen.append(c)
            in_seen.add(c)

        return "".join(seen)
