# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inordermap={val:idx for idx,val in enumerate(inorder)}
        self.pre_idx=0

        def check(left,right):
            if left>right:
                return None
            root_val=preorder[self.pre_idx]
            self.pre_idx+=1

            root=TreeNode(root_val)
            mid=inordermap[root_val]

            root.left=check(left,mid-1)
            root.right=check(mid+1,right)
            return root
        return check(0,len(inorder)-1)