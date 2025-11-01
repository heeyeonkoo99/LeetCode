from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent={}
        def dfs(node,par=None):
            if not node:
                return
            parent[node]=par
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root)

        queue=deque([(target,0)])
        visited=set([target])
        res=[]

        while queue:
            node,d=queue.popleft()
            if d==k:
                res.append(node.val)
            elif d<k:
                for neighbor in (node.left,node.right,parent[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, d+1))
        return res
        