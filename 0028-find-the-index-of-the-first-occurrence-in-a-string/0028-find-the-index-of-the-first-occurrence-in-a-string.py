class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        if haystack==needle:
            return 0
        for i in range(len(haystack)-n+1):
            if haystack[i:i+n] ==needle:
                return i
        return -1
        