class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        temp=100
        for i in nums:
            if i==target:
                return nums.index(i)
        if nums[0]>=target:
            return 0
        if nums[-1]<=target:
            return len(nums)
        for i in range(len(nums)-1):
            if nums[i]<=target and nums[i+1]>=target:
                return i+1
        
        