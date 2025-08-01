class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=set()
        rotten=set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh.add(str(i)+str(j))
                elif grid[i][j]==2:
                    rotten.add(str(i)+str(j))
        minutes=0
        directions=[[0,1],[1,0],[-1,0],[0,-1]]

        while fresh:
            infected=set()
            for orange in rotten:
                i=int(orange[0])
                j=int(orange[1])

                for direction in directions:
                    nextI=i+direction[0]
                    nextJ=j+direction[1]

                    if (str(nextI)+str(nextJ)) in fresh:
                        fresh.remove(str(nextI)+str(nextJ))
                        infected.add(str(nextI)+str(nextJ))
            if not infected:
                return -1
            rotten=infected
            minutes+=1
        return minutes