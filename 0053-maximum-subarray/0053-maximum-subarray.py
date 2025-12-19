class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=[nums[0]]
        currentsum=[nums[0]]

        for i in nums[1:]:
            currentsum=max(currentsum, currentsum+i)
            maxsum=max(maxsum,currentsum)
        return sum(maxsum)