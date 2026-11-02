class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res=[]

        i=0
        j=i
        n=len(nums)
        while j!=n:
            while j<n-1 and  nums[j+1]==nums[j]+1:
                j+=1
            start=nums[i]
            end=nums[j]

            if start==end:
                res.append(f"{start}")
            else:
                res.append(f"{start}->{end}")
            j+=1
            i=j


        return res
        