class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total=nums[0]
        current_max=nums[0]
        max_sum=current_max
        current_min=nums[0]
        min_sum=current_min

        for  i in nums[1:]:
            total+=i
            current_max=max(current_max+i,i)
            max_sum=max(current_max,max_sum)
            current_min=min(current_min+i,i)
            min_sum=min(current_min,min_sum)

        if max_sum<0:
            return max_sum
        return max(total-min_sum,max_sum)
        