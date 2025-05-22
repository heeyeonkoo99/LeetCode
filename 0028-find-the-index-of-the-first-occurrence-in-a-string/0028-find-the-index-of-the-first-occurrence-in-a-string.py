class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle=len(needle)
        if haystack==needle:
            return 0
        for i in range(0,len(haystack)-len(needle)+1):
            print(haystack[i:i+len_needle])
            if haystack[i:i+len_needle]==needle:
                return i
        return -1
        