class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(pattern) != len(s):
            return False
        p_to_s={}
        s_to_p={}
        for a,b in zip(pattern,s):
            if a in p_to_s:
                if p_to_s[a]!=b:
                    return False
            if b in s_to_p:
                if s_to_p[b]!=a:
                    return False
            
            s_to_p[b]=a
            p_to_s[a]=b
        return True
        