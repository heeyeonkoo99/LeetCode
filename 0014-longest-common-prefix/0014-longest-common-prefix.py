class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=lambda x:len(x))
        a=strs[0]

        for i in range(len(a)):
            for j in strs:
                if a[i]!=j[i]:
                    return a[:i]
        return a
        
        