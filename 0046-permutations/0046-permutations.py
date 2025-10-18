class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        visited=[False]*len(nums)

        def backtrack(current):
            if len(current)==len(nums):
                result.append(list(current))
                return
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i]=True
                    current.append(nums[i])
                    backtrack(current)
                    current.pop()
                    visited[i]=False
        backtrack([])
        return result
        
        