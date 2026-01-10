class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum=nums[0]
        maxsum=nums[0]

        for i in nums[1:]:
            currentsum=max(i,currentsum+i)
            maxsum=max(maxsum, currentsum)
        return maxsum

        