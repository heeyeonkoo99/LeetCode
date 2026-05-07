class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=nums[0]
        current_max=nums[0]
        max_sum=current_max
        current_min=nums[0]
        min_sum=current_min

        for i in nums[1:]:
            total+=i
            current_max=max(i,current_max+i)
            max_sum=max(current_max,max_sum)

            current_min=min(i,current_min+i)
            min_sum=min(current_min,min_sum)
        if max_sum<0:
            return max_sum
        return max(total-min_sum,max_sum)