# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        res=[]
        def inorder(node):
            if not node or node.left or not node.right:
                return None
            if node.left.val<node.val and node.val<node.right.val:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)
            else:
                return False
        inorder(root)
        return True

        