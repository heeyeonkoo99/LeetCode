# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def mirror(v1,v2):
            if v1 is None and v2 is None:
                return True
            if v1 is None or v2 is None:
                return False
            return v1.val==v2.val and mirror(v1.left,v2.right) and mirror(v1.right,v2.left)

        return mirror(root.left,root.right)

        