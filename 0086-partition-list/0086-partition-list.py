# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head=ListNode(0)
        after_head=ListNode(0)

        before=before_head
        after=after_head
        curr=head

        while curr:
            if curr.val<x:
                before.next=curr
                before=before.next
            else:
                after.next=curr
                after=after.next
            curr=curr.next
        after.next=None
        before.next=after_head.next
        return before_head.next        