class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer=""
        answer=s.split()
        print(answer)
        return len(answer[-1])
        