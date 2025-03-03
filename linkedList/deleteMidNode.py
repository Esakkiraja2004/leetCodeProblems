# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        total_len = 0
        curr = head 
        while curr:
            total_len += 1
            curr = curr.next

        mid = total_len // 2

        curr = head 
        out = ListNode(0)
        tail = out
        for i in range(total_len):
            if i == mid:
                curr = curr.next
            else:
                tail.next = curr
                tail = tail.next
                curr = curr.next
        tail.next = None
        return out.next
            
        
        