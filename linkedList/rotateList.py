# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        total_len = 0
        curr = head

        while curr:
            curr = curr.next
            total_len+=1
        
        if k !=0 and total_len != 0 :
            k = k % total_len
            if k == 0:
                return head 
        
        while k != 0:
            curr = head
            point = head

            for i in range(total_len-1):
                curr = curr.next
                point.val , curr.val = curr.val , point.val 
            k -= 1
        return head