class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        curr=0
        length=float('inf')
        for right in range(1,len(nums)):
            curr+=nums[right]
            while curr>=target:
                length=min(length,right-left+1)

                curr-=nums[left]
                left+=1
        return 0 if  length==float('inf') else length
                
        