class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        even=False
        if len(x)%2==0:
            even=True
        if len(x)==1:
            return True
        if even:
            for i in range((len(x)//2)):
                if x[i]!=x[len(x)-1-i]:
                    return False
            return True
        else:
            for i in range(len(x)//2):
              
                if x[i]!=x[len(x)-1-i]:
                    return False
            return True
        