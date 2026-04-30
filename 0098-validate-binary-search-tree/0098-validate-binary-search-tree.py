# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if  not node:
                return

            
            if node.left.val<node.val<node.right.val:
                return True
            inorder(node.left)
            inorder(node.right)
        inorder(root)
        return False