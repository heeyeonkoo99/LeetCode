from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a=Counter(nums)
        print(a)
        for k,v in a.items():
            if v!=1:
                return k
       