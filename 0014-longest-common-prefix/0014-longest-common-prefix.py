class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        minstr=min(strs,key=len)
        for i,s in enumerate(minstr):
            for j in strs:
                if j[i]!=s:
                    return minstr[:i]
    
        