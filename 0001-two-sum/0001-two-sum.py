class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d=dict()
        for i,v in enumerate(nums):
            if target-v in d:
                return [i,d[target-v]]
            d[v]=i


        