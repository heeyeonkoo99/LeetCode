class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        length=0
        temp=set()
        for right in range(len(nums)):
            temp.add(nums[right])
            while sum(temp)>=target:
                temp.remove(nums[left])
                left+=1

            length=min(length,right-left+1)


        return length        