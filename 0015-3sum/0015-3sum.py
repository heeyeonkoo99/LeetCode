class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1
            while left<right and  nums[i]==nums[i+1]:
                continue
            while left<right:
                temp=nums[i]+nums[left]+nums[right]
                if temp<0:
                    left+=1
                elif temp>0:
                    right-=1
                else:
                    res.append([i,left,right])
                    while left<right:
                        if nums[right]==nums[right-1]:
                            right-=1
                        elif nums[left]==nums[left+1]:
                            left+=1
                    left+=1
                    right-=1

        return res

        