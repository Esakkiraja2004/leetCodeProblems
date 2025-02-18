# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        s =  []
        curr = head
        while curr :
            s.append(str(curr.val))
            curr = curr.next
        return int("".join(s),2)