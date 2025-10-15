# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            if root==p or root==q:
                return root
            l = self.lowestCommonAncestor(root.left, p, q)
            r = self.lowestCommonAncestor(root.right, p, q)
            
            if r and l:
                return root
            elif r:
                return r
            else:
                return l

        
        