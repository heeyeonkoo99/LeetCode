class Solution:
    def reverseWords(self, s: str) -> str:
        temp=s.split()
        print(temp)
        
        a=" ".join(temp[::-1])
        return a
        
        