class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res=[]
        def dfs(start,path):
            if len(path)==k:
                res.append(path[:])
                return
            for i in range(start, n+1):
                path.append(i)
                dfs(i,path)
                path.pop()
        dfs(1,[])
        return res

        