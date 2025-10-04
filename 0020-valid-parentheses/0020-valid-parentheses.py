class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hi={"{":"}", "(":")","[":"]"}
        for i in s:
            if i in hi:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if hi[stack.pop()]!=i:
                        return False
       
        return len(stack)==0

        