from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum=defaultdict(int)
        prefix_sum[0]=1
        self.count=0

        def dfs(node, curr_sum):
            if not node:
                return
            curr_sum+=node.val

            self.count+=prefix_sum[curr_sum-targetSum]
            prefix_sum[curr_sum]+=1
            dfs(node.left,curr_sum)
            dfs(node.right,curr_sum)

            prefix_sum[curr_sum]-=1
        dfs(root,0)
        return self.count

        