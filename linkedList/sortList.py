# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arr = []
        curr = head
        while curr :
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        s = t = ListNode(0)
        for i in arr:
            s.next = ListNode(i)
            s = s.next
        return t.next

