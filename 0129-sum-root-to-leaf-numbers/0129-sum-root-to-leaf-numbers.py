# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        res=[]
        def dfs(node,path):
            if not node:
                return 0
            path=10*path+node.val
            if not node.left and node.right:
                res.append(path)
                return
            dfs(node.right,path)
            dfs(node.left,path)
            return
        dfs(root,0)
        return sum(res) 