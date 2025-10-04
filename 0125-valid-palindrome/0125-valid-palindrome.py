class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for i in s:
            if i.isalnum():  # 숫자도 포함하려면 isalnum
                temp.append(i.lower())
        
        temp = "".join(temp)
        return temp == temp[::-1]
