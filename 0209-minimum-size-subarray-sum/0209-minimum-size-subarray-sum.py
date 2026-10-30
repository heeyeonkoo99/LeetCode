class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        curr=0
        for right in range(1,len(nums)):
            while curr>=target:
                curr-=nums[left]
                left+=1
            curr+=nums[right]
        return right-left+1
                
        