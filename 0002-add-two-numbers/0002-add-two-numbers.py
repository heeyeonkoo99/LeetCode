# Definition for singly-linked list.
# class ListNode:
#      def __init__(self, val=0, next=None):
#          self.val = val
#          self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        now = l1
        while now:
            num1 = str(now.val) + num1
            now = now.next

        now = l2
        while now:
            num2 = str(now.val) + num2
            now = now.next

        result = list(str(int(num1) + int(num2)))
        print("result",result)
        answer = ListNode(int(result[0]), None)
        for i in range(1, len(result)):
            temp = ListNode(int(result[i]), answer)
            answer = temp

        return answer