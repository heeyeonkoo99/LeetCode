class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def treeDepthBalanced(node):
            if not node:
                return (0, True)
            
            l_depth, l_isbalanced = treeDepthBalanced(node.left)
            r_depth, r_isbalanced = treeDepthBalanced(node.right)
 
            isbalanced = l_isbalanced and r_isbalanced and abs(l_depth-r_depth) <= 1
            depth = max(l_depth, r_depth) + 1
 
            return (depth, isbalanced)
        
        _, isbalanced = treeDepthBalanced(root)
 
        return isbalanced