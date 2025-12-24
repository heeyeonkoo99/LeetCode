class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, best=0,0

        for i in range(len(nums)):
            if nums[i]==1:
                curr+=1
                best=max(best,curr)
            else:
                curr=0

        return best