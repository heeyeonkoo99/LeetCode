class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minstr=min(strs)
        res=""
        for i in range(len(minstr)):
            for s in strs:
                print(s[i],minstr[i])
                if s[i]!=minstr[i]:
                    return res
            res+=minstr[i]
        return res



        