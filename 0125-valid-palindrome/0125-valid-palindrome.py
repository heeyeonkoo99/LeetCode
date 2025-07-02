class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated_s=''.join(re.findall("[0-9a-z]",s.lower()))
        reversed_s=updated_s[::-1]
    
        return updated_s==reversed_s
