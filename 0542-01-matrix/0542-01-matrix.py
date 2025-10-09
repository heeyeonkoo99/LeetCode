from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=deque()
        res=[[-1]*(len(mat[0])) for _ in range( len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    res[i][j]=0
                    q.append((i,j))
        directions=[(0,1),(1,0),(-1,0),(0,-1)]

        while q:
            x,y=q.popleft()
            for dx, dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<len(mat) and 0<=ny<len(mat[0]) and res[nx][ny]==-1:
                    res[nx][ny]=res[x][y]+1
                    q.append((nx,ny))
        return res
                    


        