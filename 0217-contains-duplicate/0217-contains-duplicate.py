from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp=Counter(nums)
        for i in temp:
            if temp[i]>=2:
                return True
        return False
        