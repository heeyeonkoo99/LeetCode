class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        if not candidates or min(candidates)>target:
            return []
        def dfs(idx,out):
            if sum(out)==target:
                res.append(out[:])
                return
            elif sum(out)>target:
                return
            for i in range(idx,len(candidates)):
                out.append(candidates[i])
                dfs(i, out)
                out.pop()
        dfs(0,[])
        return res
        