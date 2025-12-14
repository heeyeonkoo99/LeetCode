class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(start,path,total):
            if total==target:
                res.append(path.copy())
                return 
            if total>target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                total+=candidates[i]
                dfs(i,path, total)
                path.pop()
                total-=candidates[i]
        dfs(0,[],0)
        return res
        