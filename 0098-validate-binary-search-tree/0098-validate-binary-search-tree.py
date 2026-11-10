# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def check(left,node,right):
            if not node:
                return
            if (left<node.val<right):
                return True
            left=self.check(left,node.left,node.val)
            right=self.check(node.val,node.right,right)
            return left and right
        return check(float("-inf"),root,float("inf"))
        