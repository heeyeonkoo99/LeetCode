from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=Counter(nums)
        for i,v in a.items():
            if v>len(nums)//2:
                return i