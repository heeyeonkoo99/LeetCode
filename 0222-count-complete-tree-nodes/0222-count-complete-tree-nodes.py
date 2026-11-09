# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        left=root
        left_h=0
        right=root
        right_h=0
        while left:
            left=left.left
            left_h+=1
        while right:
            right=right.right
            right_h+=1
        if left_h==right_h:
            return (1<<left_h)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
        