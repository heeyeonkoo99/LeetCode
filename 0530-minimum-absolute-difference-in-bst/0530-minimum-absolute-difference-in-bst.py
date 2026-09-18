# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        value=0
        res=[]
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return min(res[i+1]-res[i] for i in range(len(res)-1))
        