from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=Counter(nums)
        for i in d.items():
            if i[1]==1:
                return i[0]