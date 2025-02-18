# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        total_len = 0
        curr = head

        while curr:
            curr = curr.next
            total_len+=1

        mid = total_len // 2
    
        curr = head
        for i in range(mid):
            curr = curr.next
        return curr