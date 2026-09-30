class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=lambda x:len(x))
        res=""
   
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if strs[0][i]!=s[i]:
                    return res
            res+=strs[0][i]
        return res
        