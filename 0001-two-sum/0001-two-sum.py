class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(int)
        for i,v in enumerate(nums):
            if target-v in d:
                return [i, d[target-v]]
            d[v]=i

        