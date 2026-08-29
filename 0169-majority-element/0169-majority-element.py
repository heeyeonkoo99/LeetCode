from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=Counter(nums)
        for i,v in a.items():
            if i>=len(nums):
                return i