from collections import Counter
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a=Counter(nums)
        for i in a:
            if a[i]==2:
                return i