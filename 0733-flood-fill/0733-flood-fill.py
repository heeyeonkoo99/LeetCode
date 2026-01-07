class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n=len(image),len(image[0])
        visited=[[False]*n for _ in range(m)]
        directions=[[-1,0],[0,-1],[1,0],[0,1]]

        if image[sr][sc]==color:
            return image
        temp=image[sr][sc]

        def dfs(i,j):
            visited[i][j]=True
            for dx,dy in directions:
                x,y= i+dx,j+dy
                if 0<=x<m and 0<=y<n and visited[x][y]==False and image[x][y]==temp:
                    image[x][y]=color
                    dfs(x,y)
        image[sr][sc]=color
        dfs(sr,sc)
        return image