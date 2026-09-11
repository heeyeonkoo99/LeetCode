class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev=0
        curr=1
        cnt=0

        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                curr+=1
            else:
                cnt+=min(curr,prev)
                prev=curr
                curr=1


        cnt+=min(prev,curr)



        return cnt
        