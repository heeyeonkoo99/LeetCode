class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_value=nums[0]
        curr_value=nums[0]

        for n in nums[1:]:
            curr_value=max(n, n+curr_value)
            max_value=max(max_value,curr_value)


        return max_value