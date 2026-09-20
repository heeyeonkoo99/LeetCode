class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]

        def dfs(start,path):
            if sum(path)==target:
                res.append(path[:])
                return
            for i in range(start,target+1):
                path.append(candidates[i])
                dfs(i, path)
                path.pop()
        dfs(0,[])
        return res