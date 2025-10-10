from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}  # 원본 노드 -> 새 노드
        
        def dfs(curr):
            if curr in visited:
                return visited[curr]
            
            # 현재 노드 복사
            copy = Node(curr.val)
            visited[curr] = copy
            
            # neighbor 재귀적으로 처리
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)
        
        