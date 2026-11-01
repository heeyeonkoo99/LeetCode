class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}

        for i,v in enumerate(nums):
            if target-v in d:
                return [d[target-v],i]
            d[v]=i
        
        