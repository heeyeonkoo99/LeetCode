class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res=[]
        start=nums[0]
        end=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==start+1:
                end=nums[i]
            else:
                if start!=end:
                    res.append(format"{start}->{end}")
                else:
                    res.append(format"{start}")    
                start=nums[i]

        return res
        