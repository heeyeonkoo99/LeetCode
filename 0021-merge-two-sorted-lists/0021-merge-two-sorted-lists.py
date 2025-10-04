# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self,list1: ListNode, list2: ListNode) -> ListNode:
    # Create a dummy node
        dummy = ListNode(-1)
        # Pointer to the current node in the merged list
        current = dummy
        
        # While both lists are not empty
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If list1 is not empty, append it
        if list1:
            current.next = list1
        # If list2 is not empty, append it
        if list2:
            current.next = list2
        
        return dummy.next

            