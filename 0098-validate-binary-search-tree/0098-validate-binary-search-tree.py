# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def check(low,node,high):
            if not node:
                return True
            if not (low<node.val<high):
                return False
            return (check(low,node.left,node.val) and check(node.val,node.right,high))
        return check(float('-inf'),root,float('inf')) 
