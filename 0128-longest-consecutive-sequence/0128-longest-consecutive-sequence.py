class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        longest=0


        for n in nums:
            if n-1 not in seen:
                length=0
                while n+length not in seen:
                    seen.add(n+length)
                    length+=1
            longest=max(longest,length)
            seen.add(n)
        return longest
        