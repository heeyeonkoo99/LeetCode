class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(lambda x:key=len(x))
        a=strs[0]
        prefix=""
        for i in range(len(prefix)):
            for j in strs:
                if prefix[i]!=j[i]:
                    return prefix[:i]
        return prefix
        
        