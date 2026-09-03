class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=len(needle)
        if needle==haystack:
            return 0
        for h in range(len(haystack)):
            if haystack[h:h+l]==needle:
                return h
        return -1
        