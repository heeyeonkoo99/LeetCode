class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum=0
        left=0
        length=float("inf")
        for right in range(len(nums)):
            current_sum+=nums[right]
            while current_sum>=target:
                length=min(length,right-left+1)
                current_sum-=nums[left]
                left+=1
                
        

        return length if length!=float('inf') else 0