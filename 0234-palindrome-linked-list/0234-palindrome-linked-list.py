# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        d=deque()

        while head:
            d.append(head.val)
            head=head.next
        while len(d)>1:
            if d.popleft()!=d.pop():
                return False

        return True

