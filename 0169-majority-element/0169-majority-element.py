from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=Counter(nums)
        print(a)
        return len(Counter.values())