from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        length = 0
        odd_found = False
        
        for v in d.values():
            if v % 2 == 0:
                length += v
            else:
                length += v - 1  # 짝수 부분만 사용
                odd_found = True
        
        if odd_found:
            length += 1  # 중앙에 하나 추가
        
        return length