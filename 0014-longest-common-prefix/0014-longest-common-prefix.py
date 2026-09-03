class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        print(strs)
        
        ans=""

        for i,v in enumerate(strs[0]):
            for s in strs:
                if v!=s[i]:
                    return ans
            ans+=v

        return ans
        