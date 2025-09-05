class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def subsetsum(s,i):
            if s==0:return True
            if i>=len(nums) or s<0:return False
            return subsetsum(s-nums[i],i+1) or subsetsum(s,i+1)
        total_sum=sum(nums)
        return total_sum &1==0 and subsetsum(total_sum//2,0)
        