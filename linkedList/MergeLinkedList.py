# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # Dummy node to simplify operations
        tail = dummy  # Pointer to track the merged list

        while list1 and list2:  # Merge nodes one by one
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # Move the pointer

        # Attach the remaining nodes from list1 or list2
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next  # Return the merged list



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ls1 = []
        while list1:
            ls1.append(list1.val)
            list1 = list1.next
        
        ls2 = []
        while list2:
            ls2.append(list2.val)
            list2 = list2.next

        ls = ls1 + ls2
        ls.sort()
        s = t = ListNode()
        for i in ls:
            s.next = ListNode(i)
            s= s.next
        return t.next
        