class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        return " ".join(a[::-1])
        