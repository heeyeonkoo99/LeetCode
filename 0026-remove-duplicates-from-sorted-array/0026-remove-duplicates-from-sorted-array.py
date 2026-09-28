class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        k=1
        temp=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=temp:
                nums[k]=nums[i]
                temp=nums[k]
                k+=1
                

        return k
        