from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,m=len(s),len(p)
        res=[]
        p_counter=Counter(p)
        window_count=Counter(s[:m])

        if n<m:
            return []
        
        if p_counter==window_count:
            res.append(0)
        for i in range(m,n):
            start_char=s[i-m]
            new_char=s[i]

            window_count[new_char]+=1
            window_count[start_char]-=1
            if window_count[start_char]==0:
                del window_count[start_char]
            if window_count==p_counter:
                res.append(i-m+1)
        return res

        
        