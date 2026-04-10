class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        strs.sort(key=lambda x:len(x))

        base=strs[0]
        
        res=""

        for i in range(len(base)):
            for w in strs:
                if base[i]!=w[i]:
                    return res
            res+=base[i]








        return res
            