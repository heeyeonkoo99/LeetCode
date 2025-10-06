from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=Counter(nums)
        for i in a.values():
            if i>=2:
                return True
        return False
        