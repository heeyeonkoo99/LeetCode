class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """내가 푼 방식
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
        """
        if not strs:
            return ""
        minStr=min(strs, key=len)
        for i,x in enumerate(minStr):
            for other in strs:
                if other[i]!=x:
                    return minStr[:i]
        return minStr
        
          
            



        