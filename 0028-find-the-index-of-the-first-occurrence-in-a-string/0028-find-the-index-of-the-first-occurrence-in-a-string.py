class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack==needle:
            return 0
        n=len(needle)
        for i in range(len(haystack)-n+1):
            temp=haystack[i:i+n]
            if temp==needle:
                return i
        return -1
        

        