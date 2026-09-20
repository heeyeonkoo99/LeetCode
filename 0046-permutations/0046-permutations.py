class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res=[]
        used=[False]*len(nums)
        def dfs(path):
            if len(path)==len(nums):
                res.append(path[:])
                return
            
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                path.append(nums[i])
                dfs(path)
                path.pop()
                used[i]=False
        dfs([])


        return res
        