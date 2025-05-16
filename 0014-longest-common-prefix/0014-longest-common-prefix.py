class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small=100
        strs=sorted(strs)
        for i in strs:
            if len(i)<=small:
                small=len(i)
        for i in range(small):
            temp=strs[0][i]
            for j in strs:
                if temp!=j[i]:
                    return j[:i]
        return strs[0]
          
            



        