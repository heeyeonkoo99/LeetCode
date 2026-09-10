from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t={}
        t_to_s={}

        for a,b in zip(s,t):
            if a in s_to_t:
                if b !=s_to_t[a]:
                    return False
            if b in t_to_s:
                if a!=t_to_s[b]:
                    return False
            s_to_t[a]=b
            t_to_s[b]=a
        return True