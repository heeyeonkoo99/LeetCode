class Solution:
    def isValid(self, s: str) -> bool:
        d={"}":"{",")":"(","]":"["}
        stack=[]

        for i in s:
            if i in d and stack:
                if stack[-1]==d[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack)==0        


        