import collections
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=collections.deque()
        while head.next is not None:
            temp.append(head.val)
            head=head.next
        temp.append(head.val)
        while len(temp)>1:
            if temp.pop()!=temp.popleft():
                return False
        return True
        