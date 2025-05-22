# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder은 left->root->right의 순서를 가짐
        output=[]
        def dfs(node):
            if node:
                dfs(node.left)
                output.append(node.val)
                dfs(node.right)
        dfs(root)
        return output

        