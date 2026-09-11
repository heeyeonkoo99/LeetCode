class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        longest=0
        
        for n in seen:
            if n-1 not in seen:
                length=1
                i=1
                while n+i in seen:
                    
                    i+=1
                
                longest=max(longest,i)



        return longest


        