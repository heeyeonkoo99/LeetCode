# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev,slow,fast=None,head,head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None

        l1=self.sortList(head)
        l2=self.sortList(slow)

        return self.merge(l1,l2)

    def merge(self,l1,l2):
        dummy=tail=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
        tail.next=l1 or l2
        return dummy.next

        
        