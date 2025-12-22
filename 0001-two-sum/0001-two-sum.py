class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(int)
        for i,v in enumerate(nums):
            d[v]=i
        for i,v in enumerate(nums):
            if target-v in nums and target-v!=v:
                return [i, d[target-v]]


        