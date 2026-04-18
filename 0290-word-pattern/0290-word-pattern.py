class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_p_s={}
        map_s_p={}
        s_group=s.split()
        if len(pattern) != len(s_group):
            return False
        
        print(s)
        for p,s in zip(pattern,s_group):
            if p in map_p_s and map_p_s[p]!=s:
                return False
            if s in map_s_p and map_s_p[s]!=p:
                return False
            map_p_s[p]=s
            map_s_p[s]=p
        return True

        