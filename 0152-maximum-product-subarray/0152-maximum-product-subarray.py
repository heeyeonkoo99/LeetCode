class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=nums[0]
        min_prod=nums[0]
        result=nums[0]

        for i in nums[1:]:
            temp_max=max(i, max_prod*i, min_prod*i)
            temp_min=min(i,min_prod*i,max_prod*i)

            max_prod=temp_max
            min_prod=temp_min

            result=max(max_prod,result)
        return result