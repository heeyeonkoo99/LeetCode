from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=Counter(ransomNote)
        b=Counter(magazine)
        return True if a <= b else False

        