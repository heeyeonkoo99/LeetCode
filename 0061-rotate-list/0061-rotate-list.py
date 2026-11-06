# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0 or not head.next:
            return head
        curr=head
        length=1
        while curr.next:
            curr=curr.next
            length+=1
        k%=length
       
        steps=length-k
        curr.next=head
        new_tail=head
        for _ in range(steps-1):
            new_tail=new_tail.next
        new_head=new_tail.next
        new_tail.next=None
        return new_head


        