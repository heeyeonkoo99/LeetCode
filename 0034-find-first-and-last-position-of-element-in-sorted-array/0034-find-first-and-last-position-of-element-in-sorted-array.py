class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]

        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                res.append(mid)
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return res
        