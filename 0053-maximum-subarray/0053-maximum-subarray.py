class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currentsum=nums[0]

        for i in nums[1:]:
            currentsum=max(i, currentsum+i)
            maxsum=max(maxsum,currentsum)
        return maxsum