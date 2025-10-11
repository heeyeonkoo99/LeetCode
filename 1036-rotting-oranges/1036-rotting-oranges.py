from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        q = deque()
        
        # 1. 초기 썩은 오렌지 큐에 넣기
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))  # x, y, time

        max_time = 0
        
        # 2. BFS
        while q:
            x, y, time = q.popleft()
            max_time = max(max_time, time)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    q.append((nx, ny, time + 1))
        
        # 3. 신선한 오렌지 남아있으면 -1
        for row in grid:
            if 1 in row:
                return -1
        
        return max_time
