class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]  

        i=0
        n=len(nums)

        while i<n:
            start=nums[i]
            j=i
            while j+1<n and nums[j+1]==nums[j]+1:
                j+=1
                end=nums[j]
            if i==j:
                res.append(f"{nums[i]}")
            else:
                res.append(f"{start}->{end}")
            i=j+1


        return res
        