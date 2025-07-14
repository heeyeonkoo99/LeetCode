from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        #magazine에 있는게 ransom에 있는것보다 더 충분히 있어야함!
        for char, count in ransom_counter.items():
            if magazine_counter[char] < count:
                return False
        return True

        