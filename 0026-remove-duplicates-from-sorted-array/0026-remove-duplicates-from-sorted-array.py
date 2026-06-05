class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1

        val=nums[0]

        for i in range(1,len(nums)):
            if nums[i]!=val:
                val=nums[i]
                nums[i],nums[k]=nums[k],nums[i]
                k+=1
                

        return k
        