# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_h=0
        right_h=0
        l=root
        r=root
        while l:
            l=l.left
            left_h+=1
        while r:
            r=r.right
            right_h+=1
        if right_h==left_h:
            return (1<<left_h)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

        