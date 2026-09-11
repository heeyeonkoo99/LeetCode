class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]

        i=0
        n=len(nums)
        j=i
        while j<n:
            
         
            while j<n-1 and nums[j+1]==nums[j]+1:
                j+=1
            start=nums[i]
            end=nums[j]
            if i==j:
                res.append(f"{start}")
            else:
                res.append(f"{start}->{end}")
            j+=1
            i=j

        return res

        