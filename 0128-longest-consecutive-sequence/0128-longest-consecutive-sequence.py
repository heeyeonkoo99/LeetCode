class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set()
        longest=0
        
        for n in seen:
            if n-1 not in seen:
                longest=1
                i=1
            while n+i in seen:
                longest=max(longest,i)
                i+=1
            seen.add(n) 



        return longest


        