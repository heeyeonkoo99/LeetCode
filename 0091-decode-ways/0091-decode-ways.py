class Solution:
    def numDecodings(self, s: str) -> int:
        """
        1) single-digit deconding의 경우
        2) duoble-digit deconding의 경우
        dp를 사용한다!
        """
        if not s or s[0] == '0':
            return 0
 
        # dp[i] will store the number of ways to decode s[:i]
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # Base case: empty string
        dp[1] = 1  # Base case: single character (not '0')
    
        for i in range(2, len(s) + 1):
            # Single digit decoding
            if s[i-1] != '0':
                dp[i] += dp[i-1]
    
            # Double digit decoding
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
    
        return dp[len(s)]
