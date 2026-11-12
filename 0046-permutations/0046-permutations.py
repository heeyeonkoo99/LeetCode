class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res=[]
        visited=[False]*len(nums)
        def dfs(path):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i]=True
                path.append(nums[i])
                dfs(path)
                path.pop()
                visited[i]=False
        dfs([])
        return res
        