class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        longest=1
        length=1

        for i in range(1,len(s)):
            if ord(s[i])==ord(s[i-1])+1:
                length+=1
            else:
                length=1
            longest=max(longest,length)
        return longest