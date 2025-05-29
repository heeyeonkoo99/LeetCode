import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer=0
        collect={} 
        collect=collections.Counter(nums)
        print("collect",collect)
        for key in collect.keys():
            if collect[key]<=1:
                return key
   