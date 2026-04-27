# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=[]

        def dfs(node,path):
            if not node:
                return
            path=10*path+node.val

            if not node.left and not node.right:
                res.append(path)
                return
            dfs(node.left,path)
            dfs(node.right,path)
        dfs(root,0)

        return sum(res)