from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        a=Counter(nums)
        print()
        for i,v in a.items():
            if v>=(len(nums)/2):
                return i