from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=Counter(nums)
        for i,v in a.items():
            if v==1:
                return i