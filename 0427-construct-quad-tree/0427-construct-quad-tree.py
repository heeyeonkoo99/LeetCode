"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(x0,y0,length):
            val=grid[x0][y0]
            same=True
            for i in range(x0,x0+length):
                for j in range(y0,y0+length):
                    if grid[i][j]!=val:
                        same=False
                        break
                if not same:
                    break
            if same:
                return Node(val==1, True)
            else:
                half=length//2
                return Node(
                    True, False,
                    topLeft=helper(x0, y0, half),
                    topRight=helper(x0, y0 + half, half),
                    bottomLeft=helper(x0 + half, y0, half),
                    bottomRight=helper(x0 + half, y0 + half, half)
                )
        
        n = len(grid)
        return helper(0, 0, n)

        