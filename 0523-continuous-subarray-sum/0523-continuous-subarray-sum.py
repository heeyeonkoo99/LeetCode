class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k==0:
            for i in range(len(nums)-1):
                if nums[i]==0 and nums[i+1]==0:
                    return True
            return False
        remainder_index={0:-1}
        prefix_sum=0

        for i  in range(len(nums)):
            prefix_sum+=nums[i]
            remainder=prefix_sum%k

            if remainder in remainder_index:
                if i-remainder_index[remainder] >=2:
                    return True
            else:
                remainder_index[remainder]=i
        return False
        