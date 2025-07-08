# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #결과값은 맨 앞을 가르켜야하므로
        res = head
        def solve(root):
            if root : 
                if root.next != None and root.val == root.next.val : 
                    root.next = root.next.next
                    # 1 -> 1 -> 1 같은 중복이 연속될 경우가 있습니다.
                    solve(root)
                else:
                    solve(root.next)
        solve(head)
        return res