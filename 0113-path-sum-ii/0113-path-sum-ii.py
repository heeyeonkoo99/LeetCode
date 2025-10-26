# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]

        def dfs(node,path,total):
            if not node:
                return
            path.append(node.val)
            total+=node.val
            if not node.right and not node.left and total==targetSum:
                res.append(list(path))
            else:
                dfs(node.right,path,total)
                dfs(node.left,path,total)
            path.pop()
        dfs(root,[],0)
        return res
        