# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-float('inf'), high=float('inf')):
            # An empty tree is a valid BST
            if not node:
                return True
 
            # The current node's value must be between low and high
            if node.val <= low or node.val >= high:
                return False
    
            # Recursively validate the left and right subtree
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
    
        return validate(root)
            